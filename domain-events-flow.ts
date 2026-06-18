type ApplicationEvent = {
  id: string;
  name: string;
  entityName: string;
  payload: Record<any, any>;
  timestamp: Date;
};

type Entity = {
  id: string;
  name: string;
  events: ApplicationEvent[];
};

type EventBus = {
  events: ApplicationEvent[];
  enqueue: (event: ApplicationEvent) => boolean;
  process: () => void;
};

type EventHandler = {
  handle: (event: ApplicationEvent) => void;
};

type Mediatr = {
  getInstance: () => Mediatr;
  handlers: Record<ApplicationEvent["name"], EventHandler[]>;
  publish: (event: ApplicationEvent) => void;
  subscribe: (name: ApplicationEvent["name"], handler: EventHandler) => void;
  unsubscribe: (name: ApplicationEvent["name"], handler: EventHandler) => void;
  getHandlers: (name: ApplicationEvent["name"]) => EventHandler[];
};

class EventsMediator implements Mediatr {
  handlers: Record<ApplicationEvent["name"], EventHandler[]> = {};
  private static instance: EventsMediator | null = null;

  static getInstance(): EventsMediator {
    if (EventsMediator.instance == null) {
      EventsMediator.instance = new EventsMediator();
    }
    return EventsMediator.instance;
  }

  getInstance(): Mediatr {
    return EventsMediator.getInstance();
  }

  publish(event: ApplicationEvent): void {
    this.getHandlers(event.name).forEach((handler) => handler.handle(event));
  }

  subscribe(name: ApplicationEvent["name"], handler: EventHandler): void {
    if (!this.handlers[name]) {
      this.handlers[name] = [];
    }
    this.handlers[name].push(handler);
  }

  unsubscribe(name: ApplicationEvent["name"], handler: EventHandler): void {
    if (!this.handlers[name]) {
      return;
    }
    this.handlers[name] = this.handlers[name].filter((h) => h !== handler);
  }

  getHandlers(name: ApplicationEvent["name"]): EventHandler[] {
    return this.handlers[name] ?? [];
  }
}

class InMemoryEventBus implements EventBus {
  mediatr: Mediatr;

  events: ApplicationEvent[] = [];

  constructor(mediatr: Mediatr) {
    this.mediatr = mediatr;
  }

  static create(mediatr: Mediatr): EventBus {
    return new InMemoryEventBus(mediatr);
  }
  process(): void {
    this.events.forEach((event) => this.mediatr.publish(event));
    this.events = [];
  }

  enqueue(event: ApplicationEvent): boolean {
    this.events.push(event);
    return true;
  }
}

const userCreatedEventHandler: EventHandler = {
  handle: (event: ApplicationEvent) => {
    console.log(`User ${event.entityName} created`);
  },
};

const mediator = EventsMediator.getInstance();
mediator.subscribe("UserCreated", userCreatedEventHandler);

const eventBus = InMemoryEventBus.create(mediator);

class UserEntity implements Entity {
  id: string;
  name: string;
  events: ApplicationEvent[];

  constructor(id: string, name: string) {
    this.id = id;
    this.name = name;
    this.events = [];
  }

  save(eventBus: EventBus): void {
    this.events.forEach((event: ApplicationEvent) => {
      eventBus.enqueue(event);
    });
    eventBus.process();
    this.events = []
  }

  /**
   * Use case of creating a user and publishing the event, this is an application concern
   * @param id - The id of the user
   * @param name - The name of the user
   * @returns The user entity
   */
  static create(id: string, name: string, eventBus: EventBus): UserEntity {
    const user = new UserEntity(id, name);
    const event: ApplicationEvent = {
      id: user.id,
      name: "UserCreated",
      entityName: user.name,
      payload: {},
      timestamp: new Date(),
    };
    user.events.push(event);
    user.save(eventBus);
    return user;
  }
}
