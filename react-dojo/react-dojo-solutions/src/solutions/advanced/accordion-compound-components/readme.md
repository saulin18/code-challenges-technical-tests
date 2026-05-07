Accordion con Compound Components
Tienes un Accordion que recibe toda su configuración como props (items, activeId, onToggle). Refactorízalo al patrón Compound Components: el estado vive dentro de Accordion y los subcomponentes Accordion.Item, Accordion.Trigger y Accordion.Panel se comunican a través de Context sin recibir props explícitas entre sí.

Objetivos
1.
Crea un contexto privado AccordionCtx con { active, toggle }
2.
Accordion gestiona el estado con useState y provee el contexto
3.
Accordion.Item provee su propio id al contexto hijo con un segundo Provider (ItemCtx)
4.
Accordion.Trigger lee el id del item desde ItemCtx y llama a toggle al hacer click
5.
Accordion.Panel se renderiza solo cuando su id coincide con active
6.
La App usa la API compuesta sin pasar props entre subcomponentes