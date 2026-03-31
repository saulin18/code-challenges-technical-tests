export class Semaphore {
  private count: number;
  private queue: ((value?: void) => void)[] = [];
  private maxAllowed: number;

  constructor(maxAllowed: number) {
    this.count = 0;

    if (maxAllowed <= 0) throw new Error("Max allowed needs to be greater than 0");
    this.maxAllowed = maxAllowed;
  }

  async acquire() {
    if (this.count < this.maxAllowed) {
      this.count++;
      return Promise.resolve();
    }

    return new Promise((resolve) => {
      this.queue.push(resolve);
    });
  }

  release() {
    if (this.queue.length > 0) {
      const resolve = this.queue.shift();
      resolve?.();
      return;
    }

    this.count = Math.max(0, this.count - 1);
  }
}

export class Mutex {
  private semaphore: Semaphore;

  constructor() {
    this.semaphore = new Semaphore(1);
  }

  async acquire() {
    return this.semaphore.acquire();
  }

  release() {
    this.semaphore.release();
  }

  async withLock<T>(callback: () => Promise<T>): Promise<T> {
    await this.acquire();
    try {
      return await callback();
    } finally {
      await this.release();
    }
  }
}
