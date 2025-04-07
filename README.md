## 계속 수정해서 나갑니다다

# 🧠 CS188 Pacman 탐색 알고리즘 프로젝트

이 프로젝트는 **Introduction to Artificial Intelligence** 수업의 실습 과제로, 다양한 탐색 알고리즘을 Pacman 게임을 통해 직접 구현해보는 프로젝트입니다.

Pacman은 미로를 탐색하여 목표 지점까지 도달해야 하며, 우리는 이에 적합한 알고리즘을 구현하여 Pacman이 최적의 경로를 따라 움직이도록 만듭니다.

---

## 📁 프로젝트 구조

- `search.py`: DFS, BFS, UCS, A\* 등의 탐색 알고리즘 함수 구현
- `searchAgents.py`: Pacman이 사용할 탐색 에이전트 정의
- `pacman.py`: 게임 실행 메인 엔트리 포인트
- `autograder.py`: 구현된 알고리즘의 자동 채점기

---

## ✅ Q1: 깊이 우선 탐색 (Depth-First Search)

- 함수명: `depthFirstSearch(problem)`
- 자료구조: Stack (후입선출)
- 설명: 목표까지 도달할 수 있는 경로를 깊이 우선으로 탐색합니다. 최적 해를 보장하지는 않지만, 빠르게 결과를 찾을 수 있습니다.
- 구현 힌트:
  - `util.Stack`을 사용해 탐색 구현
  - 방문한 노드를 재방문하지 않도록 처리 필요

---

## ✅ Q2: 너비 우선 탐색 (Breadth-First Search)

- **함수명**: `breadthFirstSearch(problem)`
- **자료구조**: `Queue` (선입선출 방식)
- **설명**:  
  가까운 노드부터 차례대로 탐색하는 방식으로, 항상 **최단 경로(최소 cost)** 를 보장합니다.

- **구현 힌트**:
  - `util.Queue`를 사용해 구현
  - **방문 처리 타이밍**에 주의: 노드를 Queue에 **enqueue**할 때 방문 처리를 해야 중복 탐색을 방지할 수 있습니다.

---

## ✅ Q3: 비용 함수 기반 탐색 (Uniform Cost Search)

- **함수명**: `uniformCostSearch(problem)`
- **자료구조**: `PriorityQueue` (누적 cost 기준)
- **설명**:  
  노드까지의 **누적 비용(g(n))** 이 가장 낮은 경로를 우선적으로 탐색합니다. 항상 **최적 해**를 보장합니다.

- **구현 힌트**:
  - `util.PriorityQueue`를 사용해 구현
  - **중복 노드 처리**: 이미 방문했던 노드라도 더 낮은 cost로 도달한 경우라면 갱신해서 다시 탐색해야 합니다.

---

## ✅ Q4: A\* 탐색 (A\* Search)

- **함수명**: `aStarSearch(problem, heuristic)`
- **자료구조**: `PriorityQueue`  
  → 우선순위는 `f(n) = g(n) + h(n)`

  - `g(n)`: 시작 지점부터 현재 노드까지의 누적 비용
  - `h(n)`: 현재 노드에서 목표 지점까지의 **휴리스틱 추정 비용**

- **설명**:  
  UCS에 **휴리스틱 함수(h)** 를 결합한 알고리즘으로, 효율적이고 빠른 탐색이 가능합니다.

- **기본 휴리스틱**:

  - `nullHeuristic`: 항상 0을 반환 → UCS와 동일한 동작
  - `manhattanHeuristic`: 격자 기반의 맨해튼 거리 휴리스틱 (x, y 좌표 거리의 합)

- **구현 팁**:
  - `util.PriorityQueue`를 사용해 f(n) 기반 우선순위 큐 구성
  - `heuristic(state, problem)` 함수는 외부에서 인자로 주어짐

---

### 실행 예시

```bash
python pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch
```
