    def computeDifference(self):
        maxi = max(self.__elements)
        mini = min(self.__elements)
        self.maximumDifference = maxi - mini

 Below is the alternate Python solution:

	# Add your code here
    def computeDifference(self):
        lis = []
        for i in range(len(self.__elements)):
            for j in range(1, len(self.__elements)):
                if i == j:
                    continue
                lis.append(abs(self.__elements[i] - self.__elements[j]))
        self.maximumDifference = max(lis)
