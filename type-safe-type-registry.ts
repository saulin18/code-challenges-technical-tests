type ServiceA = Service<"ServiceA"> & {
  name: "ServiceA";
  foo: () => void;
};
type ServiceB = Service<"ServiceB"> & {
  name: "ServiceB";
  bar: () => void;
};
type Service<T extends string> = {
  __brand: T;
  createdAt?: Date | null;
  updatedAt?: Date | null;
  deletedAt?: Date | null;
  isDeleted?: boolean | null;
};

namespace WithAdditions {
  class ServiceRegistry<T extends Record<string, Service<string>>> {
    private constructor(private registry: T) {}

    //K will be always a string
    //S will be always a Service<string>
    register<K extends string, S extends Service<string>>(
      key: K,
      service: S,
      //Here we are ensuring that our ServiceRegistry is always a Record who contains the key K and the value S
    ): ServiceRegistry<T & Record<K, S>> {
    //We need to cast the registry to any to be able to assign the service to the key
      (this.registry as any)[key] = service;
      return this as unknown as ServiceRegistry<T & Record<K, S>>;
    }

    get<K extends keyof T>(key: K): T[K] {
      return this.registry[key];
    }

    delete<K extends keyof T>(key: K): void {
      delete this.registry[key];
    }

    static init(): ServiceRegistry<{}> {
      return new ServiceRegistry({});
    }
  }

  const serviceAInstance: ServiceA = {
    __brand: "ServiceA",
    name: "ServiceA",
    foo: () => {
      console.log("foo");
    },
  };
  const serviceBInstance: ServiceB = {
    __brand: "ServiceB",
    name: "ServiceB",
    bar: () => {
      console.log("bar");
    },
  };

  const registry = ServiceRegistry.init()
    .register("ServiceA", serviceAInstance)
    .register("ServiceB", serviceBInstance);

 // const a = registry.get("ServiceA")
 // const b = registry.get("ServiceB")
 //registry.delete("")
}
