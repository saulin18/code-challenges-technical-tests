import { Config } from "jest";

const config: Config = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/tests'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
  testPathIgnorePatterns: ['src/tests/helpers/', 'node_modules/', 'build/'],
  coveragePathIgnorePatterns: ['/node_modules/', 'src/tests/helpers/', 'src/infra/database/migrations/'],
  setupFilesAfterEnv: ['<rootDir>/tests/setup-db.ts'],
  moduleNameMapper: {
    '@/(.*)$': '<rootDir>/src/$1',
  },
}

export default config;