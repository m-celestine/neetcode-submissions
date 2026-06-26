class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize hash for courses and their prereqs
        prehash = {i: [] for i in range(numCourses)}

        # make a hash map that map courses to their prereq
        for course, prereq in prerequisites:
            # add prereq course to target course's list of prereq classes
            prehash[course].append(prereq)


        # inizitalize visited tracker
        visited = set()

        # dfs to traverse all courses
        def dfs(crs):
            # check already visited (for cycle/loop)
            if crs in visited:
                return False
            # quick return when course is a end
            if prehash[crs] == []:
                return True

            visited.add(crs)
            # traverse prereqs of curr course
            for pre in prehash[crs]:
                # if dfs return False , return false
                if not dfs(pre):
                    return False
            
            # if false not executed, remove crs
            visited.remove(crs)
            # update map for curr crs for easier return later
            prehash[crs] = []
            # return True
            return True

        
        #call function
        for course in range(numCourses):
            # if dfs return False , return false
            if not dfs(course):
                return False

        return True

            