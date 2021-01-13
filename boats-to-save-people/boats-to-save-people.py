class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        left = 0
        right = len(people) - 1
        no_boats = 1
        curr_size = limit
        count = 0
        while left <= right:
            
            l = people[left]
            r = people[right]
            
            if l + r <= curr_size and count < 2:
                curr_size -= l+r
                left+=1
                right-=1
                count += 2
                
                
            elif r <= curr_size and count < 2:
                curr_size -= r
                right-=1
                count+=1
            elif l<=curr_size and count < 2:
                curr_size -= l
                left += 1
                count += 1
            else:
                no_boats += 1
                curr_size = limit
                count = 0
        return no_boats
            
