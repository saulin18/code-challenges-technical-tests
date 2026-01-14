const config = {
  preset: "ts-jest",
  testEnvironment: "node",
  testPathIgnorePatterns: ["node_modules/", "build/"],
  coveragePathIgnorePatterns: ["node_modules/", "build/"],
  moduleNameMapper: {
    "@/(.*)$": "<rootDir>/src/$1",
  },
  roots: ["<rootDir>/tests", "<rootDir>"],
  testMatch: ["**/__tests__/**/*.ts", "**/?(*.)+(spec|test).ts"],
  moduleFileExtensions: ["ts", "tsx", "js", "jsx", "json"],
  transform: {
    "^.+\\.ts$": "ts-jest",
  },
};

export default config;
