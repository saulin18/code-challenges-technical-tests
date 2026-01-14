import { getTestDb } from '../../setup-db';
import { userRepository } from '../../../infrastructure/repositories/user-repository';
import { User } from '../../../domain/entities/user';

describe('UserRepository Integration Tests', () => {
  let repo: ReturnType<typeof userRepository>;

  beforeAll(() => {
    repo = userRepository(getTestDb() as any);
  });

  test('should create a user in the database', async () => {
    const userData: Omit<User, 'id' | 'createdAt' | 'updatedAt'> = {
      email: 'test@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Test',
      lastName: 'User',
      profilePicture: null,
      role: 'user',
      status: 'active',
    };

    const result = await repo.create(userData);

    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data.email).toBe('test@example.com');
      expect(result.data.firstName).toBe('Test');
      expect(result.data.lastName).toBe('User');
      expect(result.data.id).toBeDefined();
      expect(result.data.createdAt).toBeInstanceOf(Date);
      expect(result.data.updatedAt).toBeInstanceOf(Date);
    }
  });

  test('should not create a user with duplicate email', async () => {
    const userData: Omit<User, 'id' | 'createdAt' | 'updatedAt'> = {
      email: 'duplicate@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Test',
      lastName: 'User',
      profilePicture: null,
      role: 'user',
      status: 'active',
    };

    // Create first user
    const firstResult = await repo.create(userData);
    expect(firstResult.ok).toBe(true);

    const duplicateResult = await repo.create(userData);
    expect(duplicateResult.ok).toBe(false);
    if (!duplicateResult.ok) {
      expect(duplicateResult.error.message).toContain('already exists');
    }
  });

  test('should get user by email', async () => {
    const userData: Omit<User, 'id' | 'createdAt' | 'updatedAt'> = {
      email: 'getbyemail@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Test',
      lastName: 'User',
      profilePicture: null,
      role: 'user',
      status: 'active',
    };

    // Create user
    const createResult = await repo.create(userData);
    expect(createResult.ok).toBe(true);

    // Get by email
    const getResult = await repo.getByEmail('getbyemail@example.com');
    expect(getResult.ok).toBe(true);
    if (getResult.ok) {
      expect(getResult.data.email).toBe('getbyemail@example.com');
      expect(getResult.data.firstName).toBe('Test');
    }
  });

  test('should return error when user not found by email', async () => {
    const result = await repo.getByEmail('nonexistent@example.com');
    expect(result.ok).toBe(false);
    if (!result.ok) {
      expect(result.error.message).toBeDefined();
    }
  });

  test('should get user by id', async () => {
    const userData: Omit<User, 'id' | 'createdAt' | 'updatedAt'> = {
      email: 'getbyid@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Test',
      lastName: 'User',
      profilePicture: null,
      role: 'user',
      status: 'active',
    };

    // Create user
    const createResult = await repo.create(userData);
    expect(createResult.ok).toBe(true);

    if (createResult.ok) {
      // Get by id
      const getResult = await repo.getById(createResult.data.id);
      expect(getResult.ok).toBe(true);
      if (getResult.ok) {
        expect(getResult.data.id).toBe(createResult.data.id);
        expect(getResult.data.email).toBe('getbyid@example.com');
      }
    }
  });

  test('should get all users with pagination', async () => {
    // Create multiple users
    for (let i = 0; i < 5; i++) {
      await repo.create({
        email: `pagination${i}@example.com`,
        hashedPassword: 'hashed_password_123',
        firstName: `Test${i}`,
        lastName: 'User',
        profilePicture: null,
        role: 'user',
        status: 'active',
      });
    }

    // Get first page
    const result = await repo.getAll(2, 0);
    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data.length).toBe(2);
    }

    // Get second page
    const result2 = await repo.getAll(2, 2);
    expect(result2.ok).toBe(true);
    if (result2.ok) {
      expect(result2.data.length).toBe(2);
    }
  });

  test('should update user profile', async () => {
    const userData: Omit<User, 'id' | 'createdAt' | 'updatedAt'> = {
      email: 'update@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Original',
      lastName: 'Name',
      profilePicture: null,
      role: 'user',
      status: 'active',
    };

    // Create user
    const createResult = await repo.create(userData);
    expect(createResult.ok).toBe(true);

    if (createResult.ok) {
      const originalUpdatedAt = createResult.data.updatedAt;

      
      const updateResult = await repo.updateProfile({
        id: createResult.data.id,
        firstName: 'Updated',
        lastName: 'Name',
        email: 'updated@example.com',
        hashedPassword: 'hashed_password_123',
        profilePicture: null,
        role: 'user',
        status: 'active',
        createdAt: createResult.data.createdAt,
        updatedAt: new Date(),
      });

      expect(updateResult.ok).toBe(true);
      if (updateResult.ok) {
        expect(updateResult.data.firstName).toBe('Updated');
        expect(updateResult.data.lastName).toBe('Name');
        expect(updateResult.data.updatedAt.getTime()).toBeGreaterThan(originalUpdatedAt.getTime());
      }
    }
  });

  test('should soft delete user (set status to inactive)', async () => {
    const userData: Omit<User, 'id' | 'createdAt' | 'updatedAt'> = {
      email: 'delete@example.com',
      hashedPassword: 'hashed_password_123',
      firstName: 'Test',
      lastName: 'User',
      profilePicture: null,
      role: 'user',
      status: 'active',
    };

    // Create user
    const createResult = await repo.create(userData);
    expect(createResult.ok).toBe(true);

    if (createResult.ok) {
      // Delete user (soft delete)
      const deleteResult = await repo.delete(createResult.data.id);
      expect(deleteResult.ok).toBe(true);

      // Verify user still exists but is inactive
      const getResult = await repo.getById(createResult.data.id);
      expect(getResult.ok).toBe(true);
      if (getResult.ok) {
        expect(getResult.data.status).toBe('inactive');
      }
    }
  });
});
