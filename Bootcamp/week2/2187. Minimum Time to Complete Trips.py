# You are given an array time where time[i]
# denotes the time taken by the ith bus to complete one trip.

# Each bus can make multiple trips successively; that is, the next 
# trip can start immediately after completing the current trip.
# Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

# You are also given an integer totalTrips, which denotes the number of trips all buses should make in total.
# Return the minimum time required for all buses to complete at least totalTrips trips.
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start = 0
        end = min(time) * totalTrips
        while start <= end:
            mid = start + (end - start) // 2

            trips = 0
            for t in time:
                trips += mid // t

            if trips >= totalTrips:
                end = mid -1
            else:
                start = mid + 1

        return start

