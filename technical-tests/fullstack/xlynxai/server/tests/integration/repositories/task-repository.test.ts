import { getTestDb } from '../../setup-db';
import { taskRepository } from '../../../infrastructure/repositories/task-repository';
import { userRepository } from '../../../infrastructure/repositories/user-repository';
import { taskStatusesTable } from '../../../infrastructure/models/models';
import { Task } from '../../../domain/entities/tasks';
import { User } from '../../../domain/entities/user';

describe('TaskRepository Integration Tests', () => {
  let testDb: ReturnType<typeof getTestDb>;
  let taskRepo: ReturnType<typeof taskRepository>;
  let userRepo: ReturnType<typeof userRepository>;

  let testUser: User;
  let testUser2: User;
  let testStatusId: string;

  beforeAll(async () => {
    testDb = getTestDb();
    taskRepo = taskRepository(testDb as any);
    userRepo = userRepository(testDb as any);
  });

  beforeEach(async () => {
 
    const user1Result = await userRepo.create({
      email: 'taskuser1@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Task',
      lastName: 'User1',
      profilePicture: null,
      role: 'user',
      status: 'active',
    });

    const user2Result = await userRepo.create({
      email: 'taskuser2@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Task',
      lastName: 'User2',
      profilePicture: null,
      role: 'user',
      status: 'active',
    });

    if (user1Result.ok) testUser = user1Result.data;
    if (user2Result.ok) testUser2 = user2Result.data;

    // Create a task status
    const statusResult = await testDb
      .insert(taskStatusesTable)
      .values({ name: 'Test Status' })
      .returning();

    if (statusResult.length > 0) {
      testStatusId = statusResult[0].id;
    } else {
      throw new Error('Failed to create test status');
    }
  });

  test('should create a task in the database', async () => {
    if (!testUser || !testStatusId) {
      throw new Error('Test setup failed');
    }

    const taskData: Omit<Task, 'id' | 'createdAt' | 'updatedAt'> = {
      title: 'Test Task',
      description: 'Test Description',
      userId: testUser.id,
      assignedTo: testUser.id,
      statusId: testStatusId,
      startingTime: new Date(),
      endingTime: new Date(Date.now() + 86400000), 
    };

    const result = await taskRepo.create(taskData);

    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data.title).toBe('Test Task');
      expect(result.data.description).toBe('Test Description');
      expect(result.data.userId).toBe(testUser.id);
      expect(result.data.id).toBeDefined();
      expect(result.data.createdAt).toBeInstanceOf(Date);
    }
  });

  test('should get task by id', async () => {
    if (!testUser || !testStatusId) {
      throw new Error('Test setup failed');
    }

    // Create task
    const createResult = await taskRepo.create({
      title: 'Get Task',
      description: 'Get Description',
      userId: testUser.id,
      assignedTo: testUser.id,
      statusId: testStatusId,
      startingTime: new Date(),
      endingTime: new Date(),
    });

    expect(createResult.ok).toBe(true);

    if (createResult.ok) {
      // Get by id
      const getResult = await taskRepo.getById(createResult.data.id);
      expect(getResult.ok).toBe(true);
      if (getResult.ok) {
        expect(getResult.data.id).toBe(createResult.data.id);
        expect(getResult.data.title).toBe('Get Task');
      }
    }
  });

  test('should return error when task not found', async () => {
    const result = await taskRepo.getById(crypto.randomUUID());
    expect(result.ok).toBe(false);
    if (!result.ok) {
      expect(result.error.message).toContain('not found');
    }
  });

  test('should list tasks for a user', async () => {
    if (!testUser || !testStatusId) {
      throw new Error('Test setup failed');
    }

    // Create multiple tasks for the user
    for (let i = 0; i < 3; i++) {
      await taskRepo.create({
        title: `Task ${i}`,
        description: `Description ${i}`,
        userId: testUser.id,
        assignedTo: testUser.id,
        statusId: testStatusId,
        startingTime: new Date(),
        endingTime: new Date(),
      });
    }

    // List tasks
    const result = await taskRepo.list(testUser.id, 10, 0);
    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data.length).toBeGreaterThanOrEqual(3);
      result.data.forEach((task) => {
        expect(task.userId).toBe(testUser.id);
      });
    }
  });

  test('should update a task', async () => {
    if (!testUser || !testUser2 || !testStatusId) {
      throw new Error('Test setup failed');
    }

    // Create task
    const createResult = await taskRepo.create({
      title: 'Original Title',
      description: 'Original Description',
      userId: testUser.id,
      assignedTo: testUser.id,
      statusId: testStatusId,
      startingTime: new Date(),
      endingTime: new Date(),
    });

    expect(createResult.ok).toBe(true);

    if (createResult.ok) {
      const originalUpdatedAt = createResult.data.updatedAt;


      // Update task
      const updateResult = await taskRepo.update({
        id: createResult.data.id,
        title: 'Updated Title',
        description: 'Updated Description',
        assignedTo: testUser2.id,
      });

      expect(updateResult.ok).toBe(true);
      if (updateResult.ok) {
        expect(updateResult.data.title).toBe('Updated Title');
        expect(updateResult.data.description).toBe('Updated Description');
        expect(updateResult.data.assignedTo).toBe(testUser2.id);
        expect(updateResult.data.updatedAt.getTime()).toBeGreaterThanOrEqual(originalUpdatedAt.getTime());
      }
    }
  });

  test('should delete a task', async () => {
    if (!testUser || !testStatusId) {
      throw new Error('Test setup failed');
    }

    // Create task
    const createResult = await taskRepo.create({
      title: 'Delete Task',
      description: 'Delete Description',
      userId: testUser.id,
      assignedTo: testUser.id,
      statusId: testStatusId,
      startingTime: new Date(),
      endingTime: new Date(),
    });

    expect(createResult.ok).toBe(true);

    if (createResult.ok) {
      // Delete task
      const deleteResult = await taskRepo.delete(createResult.data.id);
      expect(deleteResult.ok).toBe(true);

      // Verify task is deleted
      const getResult = await taskRepo.getById(createResult.data.id);
      expect(getResult.ok).toBe(false);
    }
  });
});
