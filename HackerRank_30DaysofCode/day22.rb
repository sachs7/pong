class Node
    attr_accessor :left,:right,:data
  def initialize data
      @left=@right=nil
      @data=data
    end
end
class Solution
    def insert (root,data)
        if root==nil
            return Node.new(data)
        else
            cur=Node.new(data)
            if data<=root.data
                cur=self.insert(root.left,data)
                root.left=cur
            else
                cur=self.insert(root.right,data)
                root.right=cur
            end
        end
        return root
    end
    
    def getHeight(root)
      #Write your code here
       
        if root == nil
            return 0
        end
        left = getHeight(root.left)
        right = getHeight(root.right)
        if left > right
            return left + 1
        else
            return right + 1
        end
        
    end
end

myTree=Solution.new
root=nil
T=gets.to_i
for i in 1..T
    data=gets.to_i
    root=myTree.insert(root,data)
end
height=myTree.getHeight(root)
print height
