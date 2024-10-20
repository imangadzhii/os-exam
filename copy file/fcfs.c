#include<stdio.h>
#include<stdlib.h>
int main() {
    int n,i,j;
    int burst_time[20],wait_time[20],turn_around_time[20];
    int total_wait = 0, total_turnaround = 0;

    printf("Enter the number of process::");
    scanf("%d",&n);

    printf("Enter Burst time::\n");
    for(i=0; i<n; i++) {
        printf("process %d :",i+1);
        scanf("%d",&burst_time[i]);
    }

    wait_time[0] = 0;
    for(i=1; i<n; i++) {
        wait_time[i] = 0;
        for(j=0; j<i ;j++) {
            wait_time[i] += burst_time[j];
        }

    }

    for(i=0; i<n;i++){
        turn_around_time[i] = burst_time[i] + wait_time[i];
        total_wait += wait_time[i];
        total_turnaround += turn_around_time[i];
    }

    printf("\nprocess\t\tBurst Time\t\tWait time\t\ttotal turnaround\n");
    for(i=0;i<n;i++){
        printf("P[%d]\t\t\t%d\t\t\t\t%d\t\t\t\t%d\n",i+1,burst_time[i],wait_time[i],turn_around_time[i]);

    }

}
