import { Task } from "../../../domain/entities/tasks";

test("should create a task", () => {

  const task = Task.create({
    title: "Test Task",
    description: "Test Description",
    userId: "123",
    assignedTo: "123",
    statusId: "123",
    startingTime: new Date(),
    endingTime: new Date(),
  });
  expect(task).toBeDefined();
  expect(task.id).toBeDefined();
  expect(task.title).toBe("Test Task");
  expect(task.description).toBe("Test Description");
  expect(task.userId).toBe("123");
  expect(task.assignedTo).toBe("123");
  expect(task.statusId).toBe("123");
  expect(task.startingTime).toBeDefined();
  expect(task.endingTime).toBeDefined();

});



