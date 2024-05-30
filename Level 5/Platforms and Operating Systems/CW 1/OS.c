#include <stdio.h>
#include <stdlib.h>

// Define the ProcessControlBlock struct with four fields: pid, priority, state, and program_counter
typedef struct ProcessControlBlock {
    int pid;
    int priority;
    int state;
    int program_counter;
} ProcessControlBlock;

// Create a new ProcessControlBlock object with the given pid, priority, and program_counter values
ProcessControlBlock* create_pcb(int pid, int priority, int program_counter) {
    // Allocate memory for a new ProcessControlBlock object using the malloc function
    ProcessControlBlock* pcb = (ProcessControlBlock*) malloc(sizeof(ProcessControlBlock));
    // Set the values of the object's fields to the given arguments
    pcb->pid = pid;
    pcb->priority = priority;
    pcb->state = 0;
    pcb->program_counter = program_counter;
    // Return a pointer to the newly created object
    return pcb;
}

// Free the memory allocated to a ProcessControlBlock object
void destroy_pcb(ProcessControlBlock* pcb) {
    free(pcb);
}

// Print out the values of a ProcessControlBlock object's fields
void print_pcb(ProcessControlBlock* pcb) {
    printf("Process %d:\n", pcb->pid);
    printf("  Priority: %d\n", pcb->priority);
    printf("  State: %d\n", pcb->state);
    printf("  Program Counter: %d\n", pcb->program_counter);
}

// The main function, where the program execution begins
int main() {
    // Create a new ProcessControlBlock object with pid=1, priority=3, and program_counter=0
    ProcessControlBlock* my_pcb = create_pcb(1, 3, 0);
    // Print out the values of the my_pcb object's fields
    print_pcb(my_pcb);
    // Free the memory allocated to the my_pcb object
    destroy_pcb(my_pcb);
    // Return 0 to indicate successful program execution
    return 0;
}
