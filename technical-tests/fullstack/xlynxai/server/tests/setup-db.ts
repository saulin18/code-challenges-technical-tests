import { PGlite } from '@electric-sql/pglite';
import { drizzle } from 'drizzle-orm/pglite';
import { migrate } from 'drizzle-orm/pglite/migrator';
import * as schema from '../infrastructure/models/models';
import { join } from 'node:path';
import { existsSync } from 'node:fs';

let pglite: PGlite;
let testDb: ReturnType<typeof drizzle> | undefined;

beforeAll(async () => {
  pglite = new PGlite();
  await pglite.waitReady;
  
  testDb = drizzle(pglite, { schema });
 
  
  const migrationsFolder = join(__dirname, '..', 'drizzle');
  
  if (existsSync(migrationsFolder)) {
    await migrate(testDb, {
      migrationsFolder,
    });
  } else {
    // Note: drizzle-kit push is a CLI command, not a programmatic API
    // To set up migrations, run: drizzle-kit generate
    // Or use drizzle-kit push via CLI before running tests
    console.warn(
      `⚠️  Migrations folder not found at: ${migrationsFolder}\n` +
      '   To generate migrations, run: drizzle-kit generate\n' +
      '   Or use: drizzle-kit push (CLI command) to sync schema directly'
    );

  }
});

beforeEach(async () => {

  await pglite.exec(`
    TRUNCATE TABLE tasks, task_statuses, users RESTART IDENTITY CASCADE;
  `);
});

afterAll(async () => {
  await pglite.close();
});


export function getTestDb(): ReturnType<typeof drizzle> {
  if (!testDb) {
    throw new Error('testDb is not initialized. Make sure setup-db.ts is loaded before tests run.');
  }
  return testDb;
}

export { testDb };