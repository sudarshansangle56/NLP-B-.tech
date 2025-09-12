import java.util.*;

class RingElection {
    int numberOfProcesses;
    boolean[] active;  // keeps track of active (alive) processes
    int coordinator;

    public RingElection(int n) {
        numberOfProcesses = n;
        active = new boolean[n];
        for (int i = 0; i < n; i++) {
            active[i] = true; // all processes are initially active
        }
        coordinator = n - 1; // assume last process is the coordinator
        System.out.println("Initial Coordinator is: P" + coordinator);
    }

    // Simulate process crash
    public void crashProcess(int processId) {
        if (processId >= 0 && processId < numberOfProcesses) {
            active[processId] = false;
            System.out.println("Process P" + processId + " crashed.");
        }
    }

    // Simulate process recovery
    public void recoverProcess(int processId) {
        if (processId >= 0 && processId < numberOfProcesses) {
            active[processId] = true;
            System.out.println("Process P" + processId + " recovered.");
        }
    }

    // Ring Election Algorithm
    public void startElection(int initiator) {
        System.out.println("\nElection initiated by P" + initiator);
        int current = initiator;
        int next = (current + 1) % numberOfProcesses;
        List<Integer> electionList = new ArrayList<>();

        // circulate the message around the ring
        do {
            if (active[next]) {
                electionList.add(next);
                System.out.println("Message passed to P" + next);
            }
            next = (next + 1) % numberOfProcesses;
        } while (next != initiator);

        // highest ID becomes coordinator
        int newCoordinator = electionList.stream().max(Integer::compare).orElse(-1);
        coordinator = newCoordinator;

        // announce the coordinator
        announceCoordinator();
    }

    public void announceCoordinator() {
        System.out.println("\nNew Coordinator is: P" + coordinator);
        for (int i = 0; i < numberOfProcesses; i++) {
            if (active[i]) {
                System.out.println("P" + i + " acknowledges new coordinator P" + coordinator);
            }
        }
    }

    public static void main(String[] args) {
        RingElection ring = new RingElection(6); // 6 processes: P0, P1, ..., P5

        ring.crashProcess(5); // coordinator crashed
        ring.startElection(2); // P2 starts election

        ring.recoverProcess(5); // P5 recovers
        ring.startElection(1); // P1 starts election again
    }
}
