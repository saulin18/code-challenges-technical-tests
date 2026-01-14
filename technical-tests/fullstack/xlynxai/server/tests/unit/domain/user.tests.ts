import { User } from "../../../domain/entities/user";

test("should create a user", () => {
  const user = User.create({
    email: "test@example.com",
    hashedPassword: "password",
    firstName: "Test",
    lastName: "User",
    profilePicture: null,
    role: "user",
    status: "active",
  });

  expect(user).toBeDefined();
  expect(user.id).toBeDefined();
  expect(user.email).toBe("test@example.com");
  expect(user.hashedPassword).toBe("password");
  expect(user.firstName).toBe("Test");
  expect(user.lastName).toBe("User");
  expect(user.profilePicture).toBeNull();
  expect(user.role).toBe("user");
  expect(user.status).toBe("active");
  expect(user.createdAt).toBeDefined();
  expect(user.updatedAt).toBeDefined();
});

test("should have the correct permissions for a given role", () => {

  const user = User.create({
    email: "test@example.com",
    hashedPassword: "password",
    firstName: "Test",
    lastName: "User",
    profilePicture: null,
    role: "user",
    status: "active",
  });

  const userPermissions = User.getPermissions(user)

  const permissionsGivenUserRole = []
  permissionsGivenUserRole.push(`tasks::read::owner:${user.id}`);
  permissionsGivenUserRole.push(`tasks::write::owner:${user.id}`);
  permissionsGivenUserRole.push(`users::read::owner:${user.id}`);

  expect(userPermissions).toBeDefined()
  expect(userPermissions).toEqual(permissionsGivenUserRole)

  const adminUser = User.create({
    email: "admin@example.com",
    hashedPassword: "password",
    firstName: "Admin",
    lastName: "User",
    profilePicture: null,
    role: "admin",
    status: "active",
  });

  const adminPermissions = User.getPermissions(adminUser);

  const permissionsGivenAdminRole = [
    "tasks::all::all",
    "users::all::all"
  ];

  expect(adminPermissions).toBeDefined();
  expect(adminPermissions).toEqual(permissionsGivenAdminRole);
});
