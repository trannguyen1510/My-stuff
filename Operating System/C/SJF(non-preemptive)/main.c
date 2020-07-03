#include<stdio.h>
int mat[10][6];

void swapping(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void SortArr(int num, int mat[][6])
{
    for(int i=0; i<num; i++)
    {
        for(int j=0; j<num-i-1; j++)
        {
            if(mat[j][1] > mat[j+1][1])
            {
                for(int k=0; k<5; k++)
                {
                    swapping(&mat[j][k], &mat[j+1][k]);
                }
            }
        }
    }
}

void FinishTime(int num, int mat[][6])
{
    int temp, val;
    mat[0][3] = mat[0][1] + mat[0][2];
    mat[0][5] = mat[0][3] - mat[0][1];
    mat[0][4] = mat[0][5] - mat[0][2];

    for(int i=1; i<num; i++)
    {
        temp = mat[i-1][3];
        int low = mat[i][2];
        for(int j=i; j<num; j++)
        {
            if(temp >= mat[j][1] && low >= mat[j][2])
            {
                low = mat[j][2];
                val = j;
            }
        }
        mat[val][3] = temp + mat[val][2];
        mat[val][5] = mat[val][3] - mat[val][1];
        mat[val][4] = mat[val][5] - mat[val][2];
        for(int k=0; k<6; k++)
        {
            swapping(&mat[val][k], &mat[i][k]);
        }
    }
}

int main()
{
    int num;

    printf("Enter number of Process: ");
    scanf("%d", &num);

    for(int i=0; i<num; i++)
    {
        printf("Enter the Process Name, Arrival Time & Burst Time: ");
        scanf("%d%d%d",&mat[i][0],&mat[i][1],&mat[i][2]);
    }

    SortArr(num, mat);
    FinishTime(num, mat);
    printf("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n");
    for(int i=0; i<num; i++)
    {
        printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n",mat[i][0],mat[i][1],mat[i][2],mat[i][4],mat[i][5]);
    }
    printf("\nIn non-preemptive SJF: Respond Time = Waiting Time\n");

    double aver_wait_time = 0;
    for (int i=0; i<num; i++)
    {
        aver_wait_time += mat[i][4];
    }
    aver_wait_time /= num;
    printf("\nAverage Waiting Time = %f", aver_wait_time);

    double aver_turn_time = 0;
    for (int i=0; i<num; i++)
    {
        aver_turn_time += mat[i][5];
    }
    aver_turn_time /= num;
    printf("\nAverage Turnaround Time = %f", aver_turn_time);
}
