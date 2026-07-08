class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        callStack = []

        cpuTime = [0] * n

        lastTimestamp = 0

        for idx, log in enumerate(logs):
            function_id, event, timestamp = log.split(":")
            timestamp = int(timestamp)
            function_id = int(function_id)

            if event == "start":
                if callStack:
                    elapsed = timestamp - lastTimestamp
                    cpuTime[callStack[-1]] += elapsed
                callStack.append(function_id)
                lastTimestamp = timestamp
            elif event == "end":
                elapsed = timestamp - lastTimestamp + 1
                cpuTime[callStack[-1]] += elapsed
                callStack.pop()
                lastTimestamp = timestamp + 1

        return cpuTime
