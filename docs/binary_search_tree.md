* 二分搜索树是二叉树。
* 二分搜索树的每个节点的值大于其左子树的所有节点的值，并且小于其右子树的所有节点的值。
* 每一颗子树也是二分搜索树。

#### 二叉树的非递归访问

```cpp
// in-order
void InOrderNR(BTNode* root) {
	//空树
	if (root == NULL)
		return;
	//树非空
	BTNode* p = root;
	stack<BTNode*> s;
	while (!s.empty() || p) {
		//一直遍历到左子树最下边，边遍历边保存根节点到栈中
		while (p)
		{
			s.push(p);
			p = p->lchild;
		}
		//当p为空时，说明已经到达左子树最下边，这时需要出栈了
		if (!s.empty())
		{
			p = s.top();
			s.pop();
			cout  << p->data << endl;
			//进入右子树，开始新的一轮左子树遍历(这是递归的自我实现)
			p = p->rchild;
		}
	}
}
```

```cpp
// pre-order
void PreOrderNR(BTNode* root) {
    if (root == NULL) return;
    BTNode* p = root;
    stack<BTNode*> s;
    s.push(p);
    while (!s.empty()) {
        p = s.top();
        s.pop();
        cout << p->data << endl;
        if (p->rchild != NULL)
            s.push(p->rchild);
        if (p->lchild != NULL)
            s.push(p->lchild);
    }
}
```

```cpp
// post-order
void PostOrderWithoutRecursion(BTNode* root)
{
    if (root == NULL)
        return;
    stack<BTNode*> s;
    // pCur:当前访问节点，pLastVisit:上次访问节点
    BTNode* pCur, *pLastVisit;
    pCur = root;
    pLastVisit = NULL;
    // 先把pCur移动到左子树最下边
    while (pCur)
    {
        s.push(pCur);
        pCur = pCur->lchild;
    }
    while (!s.empty())
    {
        // 走到这里，pCur为空，并已经遍历到左子树底端(看成扩充二叉树，则空，亦是某棵树的左孩子)
        pCur = s.top();
        s.pop();
        // 一个根节点被访问的前提是：无右子树或右子树已被访问过
        if (pCur->rchild == NULL || pCur->rchild == pLastVisit)
        {
            cout << pCur->data << endl;
            // 修改最近被访问的节点
            pLastVisit = pCur;
        }
        /*
         这里的else语句可换成带条件的else if:
         else if (pCur->lchild == pLastVisit)//若左子树刚被访问过，则需先进入右子树(根节点需再次入栈)
         因为：上面的条件没通过就一定是下面的条件满足。
         */
        else
        {
            // 根节点再次入栈
            s.push(pCur);
            // 进入右子树，且可肯定右子树一定不为空
            pCur = pCur->rchild;
            while (pCur)
            {
                s.push(pCur);
                pCur = pCur->lchild;
            }
        }
    }
}
```
