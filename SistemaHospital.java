import java.io.*;
import java.time.LocalDate;
import java.util.*;

public class SistemaHospital implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private List<Paciente> pacientes;
    private List<Doctor> doctores;
    private List<Consulta> consultas;

    public SistemaHospital() {
        this.pacientes = new ArrayList<>();
        this.doctores = new ArrayList<>();
        this.consultas = new ArrayList<>();
    }

    public void agregarPaciente(Paciente p) {
        pacientes.add(p); 
    }

    public List<Paciente> getPacientes() {
        return pacientes;
    
    }
    public Paciente buscarPacientePorCI(String ci) {
        for (Paciente p : pacientes) {
            if (p.getCi().equals(ci)) {
                return p;
            }
        }
        return null;
    }

    public void eliminarPaciente(Paciente p) {
        pacientes.remove(p);
    }

    public void agregarDoctor(Doctor d) {
        doctores.add(d);
    }

    public List<Doctor> getDoctores() {
        return doctores;
    }

    public Doctor buscarDoctorPorNombre(String nombre) {
        for (Doctor d : doctores) {
            if (d.getNombre().equalsIgnoreCase(nombre)) return d;
        }
        return null;
    }
    
    public void eliminarDoctor(Doctor d) {
        doctores.remove(d);
    }

    public void agregarConsulta(Consulta c) {
        consultas.add(c);
    }

    public List<Consulta> getConsultas() {
        return consultas;
    }

    public void eliminarConsulta(Consulta c) {
        consultas.remove(c);
    }

    public Deque<Paciente> pacientesAtendidosEnDia(LocalDate fecha) {
        Deque<Paciente> pacientesDelDia = new ArrayDeque<>();
        for (Consulta c : consultas) {
            if (c.getFecha().equals(fecha)) {
                if (!pacientesDelDia.contains(c.getPaciente())) {
                    pacientesDelDia.addLast(c.getPaciente());
                }
            }
        }
        return pacientesDelDia;
    }

    public List<Consulta> consultasPorPaciente(String ci) {
        List<Consulta> historial = new ArrayList<>();
        for (Consulta c : consultas) {
            if (c.getPaciente().getCi().equals(ci)) {
                historial.add(c);
            }
        }
        return historial;
    }

    public void mostrarExtremosEdad() {
        if (pacientes.isEmpty()) {
            System.out.println("No hay pacientes registrados.");
            return;
        }
        
        List<Paciente> copia = new ArrayList<>(pacientes);
        quickSortPorEdad(copia, 0, copia.size() - 1);

        Paciente masJoven = copia.get(0);
        Paciente masViejo = copia.get(copia.size() - 1);

        System.out.println("Paciente más joven: " + masJoven.getNombre() + " (" + masJoven.getEdad() + " años)");
        System.out.println("Paciente más viejo: " + masViejo.getNombre() + " (" + masViejo.getEdad() + " años)");
    }

    private void quickSortPorEdad(List<Paciente> lista, int low, int high) {
        if (low < high) {
            int pi = partition(lista, low, high);
            quickSortPorEdad(lista, low, pi - 1);
            quickSortPorEdad(lista, pi + 1, high);
        }
    }

    private int partition(List<Paciente> lista, int low, int high) {
        int pivot = lista.get(high).getEdad();
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (lista.get(j).getEdad() < pivot) {
                i++;
                Paciente temp = lista.get(i);
                lista.set(i, lista.get(j));
                lista.set(j, temp);
            }
        }
        Paciente temp = lista.get(i + 1);
        lista.set(i + 1, lista.get(high));
        lista.set(high, temp);
        return i + 1;
    }

    public String generarHistoriaClinica(String ci) {
        Paciente p = buscarPacientePorCI(ci);
        if (p == null) return "Paciente no encontrado.";
        
        StringBuilder hc = new StringBuilder();
        hc.append("=== HISTORIA CLÍNICA ===\n");
        hc.append(p.getDetalles()).append("\n");
        hc.append("Consultas Asistidas:\n");
        
        boolean tieneConsultas = false;
        for (Consulta c : consultas) {
            if (c.getPaciente().getCi().equals(ci)) {
                hc.append("- Fecha: ").append(c.getFecha()).append(" | Dr. ").append(c.getDoctor().getNombre())
                  .append("\n  Notas: ").append(c.getNotas()).append("\n");
                tieneConsultas = true;
            }
        }
        
        if (!tieneConsultas) hc.append("Ninguna consulta registrada.");
        return hc.toString();
    }

    public void guardarEstado(String archivo) throws IOException {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(archivo))) {
            out.writeObject(this);
        }
    }

    public static SistemaHospital cargarEstado(String archivo) throws IOException, ClassNotFoundException {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(archivo))) {
            return (SistemaHospital) in.readObject();
        }
    }
}