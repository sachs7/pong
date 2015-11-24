Problem Statement

Let's consider a standard darts target that consists of K concentric circles with the corresponding radiuses R1,R2,...,RK with the common center in the origin (0,0).

If your shot lands inside the smallest circle, you will get K points. Landing between the ith and the (i+1)th circle will give you i points. This means your shot includes the ith circle, but excludes the (i+1)th circle. If the shot lands on the boundary of the circle, it will be considered to have landed inside that circle.

Finally, if you are unable to land inside or on the boundary of the 1st circle, you will get 0 points for that shot.

You are given coordinates xi,yi of N shots. Calculate the final score (the sum of all the points).

Input Format

The first line contains two space-separated integers: K and N.

The second line contains K space-separated integers: R1,R2,...RK.

The following N lines contain two-space separated integers xi, yi, the coordinates of the ith shot.

Constraints

1≤K≤104 1≤N≤5×105 1≤RK<RK−1<...<R1≤5×104 |xi|,|yi|≤5×104 In test data worth 40% of points, 1≤N≤103 holds in addition.

Output Format

Output one integer on a single line: The sum of all the points scored.

Sample Input

5 6 
10 8 6 4 2 
0 0 
1 1 
2 2 
3 3 
4 4 
5 5 

Sample Output

22 

Explanation

The partial scores are: 5+5+4+3+3+2=22
