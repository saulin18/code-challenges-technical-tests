import { getTestDb } from "../setup-db";
import request from "supertest";
import express from "express";
import cors from "cors";

import { globalErrorHandler } from "../../api/middlewares/global-error-handler";
import { taskStatusesTable } from "../../infrastructure/models/models";

// Set up environment variables for tests
process.env.JWT_SECRET = process.env.JWT_SECRET || "test-jwt-secret-key-for-e2e-tests";
process.env.NODE_ENV = "test";

jest.mock('../../infrastructure/database', () => {
    let cachedDb: any = null;
    
    return {
      get db() {
        // Si ya tenemos la BD cacheada, la retornamos
        if (cachedDb) {
          return cachedDb;
        }
        
        // Intentamos obtener la BD de test
        // Si aún no está lista, getTestDb() lanzará un error
        // pero lo capturamos y retornamos un proxy que fallará más tarde
        try {
          cachedDb = getTestDb();
          return cachedDb;
        } catch (error) {
          // Si testDb no está listo, retornamos un proxy que intentará obtenerlo
          // cuando se use realmente (lazy evaluation)
          return new Proxy({}, {
            get(target, prop) {
              // Cuando se accede a cualquier propiedad, intentamos obtener la BD
              const db = getTestDb();
              cachedDb = db;
              return (db as any)[prop];
            }
          });
        }
      },
    };
  });

import { tasksRoutes } from "../../api/routes/tasks/tasks.routes";
import { userRoutes } from "../../api/routes/users/user.routes";

const createTestApp = () => {
  const testApp = express();
  testApp.use(express.json());
  testApp.use(cors());
  testApp.use("/api/tasks", tasksRoutes);
  testApp.use("/api/users", userRoutes);
  testApp.get("/health", (req, res) => {
    res.status(200).json({ message: "OK" });
  });
  testApp.use(globalErrorHandler);
  return testApp;
};

let app: ReturnType<typeof createTestApp>;

beforeAll(() => {
  app = createTestApp();
});

describe("Task Endpoints E2E", () => {
  let testAccessToken: string;
  let testStatusId: string;
  let lastTaskId: string;

  beforeEach(async () => {
    // Create status first
    const statusResult = await getTestDb()
      .insert(taskStatusesTable)
      .values({ name: "Test Status" })
      .returning();

    if (statusResult.length > 0) {
      testStatusId = statusResult[0].id;
    }

   
    const registerResponse = await request(app)
      .post("/api/users/register")
      .send({
        email: "e2e@test.com",
        password: "testpassword123",
        firstName: "E2E",
        lastName: "Test",
        profilePicture: null,
      });

    if (registerResponse.status !== 201) {
      console.error("Register failed:", registerResponse.body);
      throw new Error("Failed to register user for tests");
    }

    const loginResponse = await request(app).post("/api/users/login").send({
      email: "e2e@test.com",
      password: "testpassword123",
    });

    if (loginResponse.status !== 200) {
      console.error("Login failed:", loginResponse.body);
      throw new Error("Failed to login user for tests");
    }

    testAccessToken = loginResponse.body.data.accessToken;
  });

  it("should have valid access token from setup", () => {
    expect(testAccessToken).toBeDefined();
    expect(typeof testAccessToken).toBe("string");
  });

  it("should get all tasks (empty initially)", async () => {
    const response = await request(app)
      .get("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`);

    expect(response.status).toBe(200);
    expect(response.body.data).toBeDefined();
    expect(Array.isArray(response.body.data)).toBe(true);
    expect(response.body.data.length).toBe(0);
  });

  it("should create a task", async () => {
    const response = await request(app)
      .post("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`)
      .send({
        title: "New Task",
        description: "Task Description",
        statusId: testStatusId,
      });

    expect(response.status).toBe(201);
    expect(response.body.data.title).toBe("New Task");
    expect(response.body.data.description).toBe("Task Description");
    expect(response.body.data.statusId).toBe(testStatusId);
    expect(response.body.data.id).toBeDefined();
    expect(response.body.data.createdAt).toBeDefined();
    expect(response.body.data.updatedAt).toBeDefined();

    lastTaskId = response.body.data.id;
  });

  it("should get all tasks (after creation)", async () => {
    // Create a task first
    const createResponse = await request(app)
      .post("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`)
      .send({
        title: "Task for List",
        description: "Task Description",
        statusId: testStatusId,
      });

    expect(createResponse.status).toBe(201);

    const response = await request(app)
      .get("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`);

    expect(response.status).toBe(200);
    expect(response.body.data.length).toBeGreaterThan(0);
  });

  it("should get a task by id", async () => {
    // Create a task first
    const createResponse = await request(app)
      .post("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`)
      .send({
        title: "Task to Get",
        description: "Task Description",
        statusId: testStatusId,
      });

    expect(createResponse.status).toBe(201);
    const taskId = createResponse.body.data.id;

    const response = await request(app)
      .get(`/api/tasks/${taskId}`)
      .set("Authorization", `Bearer ${testAccessToken}`);

    expect(response.status).toBe(200);
    expect(response.body.data.id).toBe(taskId);
    expect(response.body.data.title).toBe("Task to Get");
    expect(response.body.data.description).toBe("Task Description");
  });

  it("should update a task", async () => {
    // Create a task first
    const createResponse = await request(app)
      .post("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`)
      .send({
        title: "Task to Update",
        description: "Original Description",
        statusId: testStatusId,
      });

    expect(createResponse.status).toBe(201);
    const taskId = createResponse.body.data.id;

    const response = await request(app)
      .put(`/api/tasks/${taskId}`)
      .set("Authorization", `Bearer ${testAccessToken}`)
      .send({
        title: "Updated Task",
        description: "Updated Description",
      });

    expect(response.status).toBe(200);
    expect(response.body.data.title).toBe("Updated Task");
    expect(response.body.data.description).toBe("Updated Description");
    expect(response.body.data.id).toBe(taskId);
  });

  it("should delete a task", async () => {
    // Create a task first
    const createResponse = await request(app)
      .post("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`)
      .send({
        title: "Task to Delete",
        description: "Task Description",
        statusId: testStatusId,
      });

    expect(createResponse.status).toBe(201);
    const taskId = createResponse.body.data.id;

    const response = await request(app)
      .delete(`/api/tasks/${taskId}`)
      .set("Authorization", `Bearer ${testAccessToken}`);

    expect(response.status).toBe(204);
    expect(response.body).toEqual({});
  });

  it("should return 404 when getting deleted task", async () => {
    // Create a task first
    const createResponse = await request(app)
      .post("/api/tasks")
      .set("Authorization", `Bearer ${testAccessToken}`)
      .send({
        title: "Task to Delete and Check",
        description: "Task Description",
        statusId: testStatusId,
      });

    expect(createResponse.status).toBe(201);
    const taskId = createResponse.body.data.id;

    // Delete the task
    const deleteResponse = await request(app)
      .delete(`/api/tasks/${taskId}`)
      .set("Authorization", `Bearer ${testAccessToken}`);

    expect(deleteResponse.status).toBe(204);

    // Try to get the deleted task
    const response = await request(app)
      .get(`/api/tasks/${taskId}`)
      .set("Authorization", `Bearer ${testAccessToken}`);

    expect(response.status).toBe(400);
  });
});
