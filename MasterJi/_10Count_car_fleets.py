class Solution:
    def countCarFleets(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        Calculates the number of car fleets that reach the destination.
        
        Time Complexity: O(n log n) due to sorting the positions.
        Space Complexity: O(n) to store position-speed pairs and the stack.
        """
        # Combine position and speed into pairs and sort by position descending
        # We process cars from the one closest to the target to the furthest
        cars = sorted(zip(position, speed), reverse=True)
        
        # This stack will store the arrival times of the fleet leaders
        fleet_times = []
        
        for p, s in cars:
            # Time = (Distance to target) / Speed
            arrival_time = (target - p) / s
            
            # If the current car takes MORE time than the fleet in front of it,
            # it can't catch up, so it starts a new fleet.
            if not fleet_times or arrival_time > fleet_times[-1]:
                fleet_times.append(arrival_time)
            
            # If arrival_time <= fleet_times[-1], the car catches up to the fleet
            # in front and its speed is limited by that fleet's leader.
            # We don't need to do anything as it joins the existing fleet.

        return len(fleet_times)

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1:
    # Target: 50, Pos: [10, 20, 30], Speed: [3, 2, 1]
    # Times: (50-10)/3=13.33, (50-20)/2=15, (50-30)/1=20
    # Sorted by Pos: (30, 1) -> Time 20; (20, 2) -> Time 15; (10, 3) -> Time 13.33
    # All cars behind 30 take less time, so they catch up. Result: 1
    sol.countCarFleets(50, [10, 20, 30], [3, 2, 1])

    # Example 2: Target 12, Standard multi-fleet case
    pos2 = [10, 8, 0, 5, 3]
    spd2 = [2, 4, 1, 1, 3]
    # Sorted: (10,2) T=1.0; (8,4) T=1.0; (5,1) T=7.0; (3,3) T=3.0; (0,1) T=12.0
    # Fleet 1: Time 1.0 (Cars at 10 and 8)
    # Fleet 2: Time 7.0 (Cars at 5 and 3)
    # Fleet 3: Time 12.0 (Car at 0)
    sol.countCarFleets(12, pos2, spd2) # Expected: 3

    # Example 3: Single car
    sol.countCarFleets(100, [10], [10]) # Expected: 1