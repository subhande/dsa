# Job Sequencing Problem

class Solution:
    def JobScheduling(self, Jobs):
        Jobs.sort(key=lambda x: x[2], reverse=True)
        n = len(Jobs)
        currentTime = 0
        noOfJobsCompleted = 0
        totalProfit = 0
        timeline = [-1] * n
        for idx in range(n):
            job = Jobs[idx]
            for j in range(job[1] - 1, -1, -1):
                if timeline[j] == -1:
                    noOfJobsCompleted += 1
                    totalProfit += job[2]
                    currentTime += 1
                    timeline[j] = job[0]
                    break
        return noOfJobsCompleted, totalProfit


class Solution2:
    def JobScheduling(self, Jobs):
        # Sort jobs based on profit in descending order
        Jobs.sort(key=lambda x: x[2], reverse=True)

        # Total number of jobs
        n = len(Jobs)

        """Initialize a hash table
        to store selected jobs.
        each element represents a
        deadline slot,
        initially unoccupied."""
        hash = [-1] * n

        # Initialize count
        cnt = 0

        # Initialize the total profit earned
        totalProfit = 0

        # Iterate over each job
        for i in range(n):
            """Iterate over each deadline slot starting
            from the job's deadline"""
            for j in range(Jobs[i][1] - 1, -1, -1):
                """If the current deadline
                slot is available
                (not occupied)"""
                if hash[j] == -1:
                    # Count of selected jobs
                    cnt += 1
                    # Mark the job as selected
                    hash[j] = Jobs[i][0]
                    # Update the total profit
                    totalProfit += Jobs[i][2]
                    # Move to the next job
                    break

        # Return the list
        return [cnt,totalProfit]
