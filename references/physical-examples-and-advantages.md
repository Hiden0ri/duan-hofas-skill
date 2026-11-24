# FAS 物理背景、具体动力学/全驱转化形式与优势手册

本手册系统汇总 `duan-hofas` **一级权威库（36 篇 Duan 一作 + 2026 *Volume I*）** 与 **二级分级后备库（重点选取 Score 5 / Score 4 旗舰期刊及关键 Score 3 期刊）** 中的典型物理对象、原始动力学方程、HOFAS / sub-FAS / UC-FAS / OD-FAS 具体转化形式、奇异集/可行集、代表仿真参数，以及 **FAS 方法在各具体背景上的优势与客观边界**。

> **使用与溯源纪律**：
> - 全部模型与优势论断均来自库内原文 `[E]`，已标注 `doc_id`、分值（`Primary` 表示一级权威库；`S5`/`S4`/`S3` 表示二级后备库分值）及原文献定位。
> - **切勿把二级库中社区作者的新构造、新术语或特定场景假设归于段广仁原文名下**；引用非 Duan 论文时须署名原论文作者。
> - 按数学结构选例请配合 [example-library.md](example-library.md)，全量 3–5 分期刊应用清单见 `corpus/sorted/physical_examples_catalog.md`，FAS 通用方法优势原文句库见 [fas-advantages-corpus.md](fas-advantages-corpus.md)。

---

## 一、航天器与空天飞行器

### 1.1 刚体航天器欧拉角姿态系统（二阶 sub-FAS）
- **来源**：`ijss_2022_part8` §6（Primary / S5，*IJSS* 2022, p.13–15）
- **原始动力学形式**（$Z(\psi)\to X(\phi)\to Y(\vartheta)$ 旋转序，$q=[\phi,\vartheta,\psi]^\top$ 为滚转/俯仰/偏航角，$u\in\mathbb{R}^3$ 为控制力矩）：
  $$M(q)\ddot q + D(q,\dot q)\dot q + \xi(q,\dot q) = u, \quad M(q)=\begin{bmatrix} I_x\cos\vartheta & 0 & -I_x\cos\phi\sin\vartheta \\ 0 & I_y & I_y\sin\phi \\ I_z\sin\vartheta & 0 & I_z\cos\phi\cos\vartheta \end{bmatrix}.$$
- **HOFAS / sub-FAS 转化形式**：自然二阶全驱（无需降阶为一阶状态空间），直接改写为标准二阶 sub-FAS：
  $$\ddot q = f(q,\dot q) + B(q)u, \quad f(q,\dot q)=-M^{-1}(q)[D(q,\dot q)\dot q+\xi(q,\dot q)], \quad B(q)=M^{-1}(q).$$
- **奇异集 / 可行集**：$\det B(q)=\dfrac{1}{I_x I_y I_z\cos\phi}$，奇异集为
  $$\mathbb{S}=\left\{q\in\mathbb{R}^3 \;\middle|\; \phi = \pm\frac{(2k+1)\pi}{2},\; k=0,1,2,\ldots\right\}, \quad d_0 = \frac{\pi}{2}.$$
- **代表仿真参数**：$I_x=18,\; I_y=21,\; I_z=24$；权重 $Q_a=\mathrm{diag}(1,2.5),\; Q_b=\gamma I_4,\; R_b=I_2$；滚转通道与俯仰/偏航通道解耦优化后初值可行域显式给出为 $\phi^2(0)+\dot\phi^2(0)<0.9415$（初值例 $\phi(0)=0.5236,\dot\phi(0)=-0.2104,\vartheta(0)=-2\pi/3,\dot\vartheta(0)=1.2$）。
- **FAS 在该背景上的优势 `[E]`**：
  1. 保留拉格朗日/牛顿-欧拉二阶物理结构，直接消去全部科氏与惯量耦合非线性，将姿态控制化为解耦的线性定常闭环 $\ddot\phi=v_a,\; [\ddot\vartheta,\ddot\psi]^\top=v_b$；
  2. 将奇异变量 $\phi$ 与非奇异通道 $(\vartheta,\psi)$ 解耦设计二次最优指标（仅对 $\phi$ 通道施加 RoEA 初值约束），显著扩大允许的俯仰/偏航初始范围并保持平稳低加速度机动。
- **适用前提与局限边界 `[E]`**：依赖惯量矩阵 $M(q)$ 精度；欧拉角表示固有 $|\phi|<\pi/2$ 奇异面，大角度无退绕机动需结合四元数/MRP/Twistor 表示（见 1.4 节）及干扰观测器。

### 1.2 两推力矩欠驱动刚体航天器（Brockett 第一反例 / sub-FAS）
- **来源**：`tcyb_2023_subfas` Ex. 2（Primary / S5，*IEEE TCYB* 2023, p.3–4）；`jssc_2022_brockett1` §1.1 & §3（Primary / S5，*JSSC* 2022, p.2–5）
- **原始动力学形式**（三主轴中仅两轴有控制力矩 $\tau_1,\tau_2$，第三轴非对称 $J_1\neq J_2$）：
  $$J_1\dot\omega_1 = (J_2-J_3)\omega_2\omega_3+\tau_1,\quad J_2\dot\omega_2 = (J_3-J_1)\omega_3\omega_1+\tau_2,\quad J_3\dot\omega_3 = (J_1-J_2)\omega_1\omega_2.$$
- **sub-FAS 转化形式**：令 $a=(J_1-J_2)/J_3\neq 0$，$(x,y,z)=(a\omega_1,\omega_2,\omega_3)$ 及输入变换化为 Brockett 第一反例 $\dot x=u_1,\;\dot y=u_2,\;\dot z=xy$。在 $y(t)\neq 0$ 上消去 $x=\dot z/y$ 得混阶 sub-FAS：
  $$\begin{bmatrix}\ddot z \\ \dot y\end{bmatrix} = \begin{bmatrix} y & \dot z/y \\ 0 & 1 \end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}.$$
- **奇异集 / 可行集**：综合两个坐标分支可得几乎全局可行集 $\mathbb{F}=\{(x_0,y_0,z_0)^\top\in\mathbb{R}^3 \mid x_0^2+y_0^2\neq 0\}$（仅剔除 $z_0$ 轴一条直线）。
- **FAS 在该背景上的优势 `[E]`**：
  1. 经典结论表明该系统不可反馈线性化且不存在光滑指数镇定律（线性化不可镇定）；传统光滑反馈（Brockett / Byrnes–Isidori）只能非指数渐近收敛。
  2. 通过 sub-FAS 亚镇定，仅用**光滑时不变反馈**即可在除去 $z_0$ 轴的全空间实现**指数收敛**，且吸引域无界、边界精确刻画；若初值恰落 $z_0$ 轴，仅需极简预控制器作微小机动推离 $z_0$ 轴即可切换接管实现全局镇定。
- **适用前提与局限边界 `[E]`**：要求 $J_1\neq J_2$（欠驱动轴非对称轴）；纯单一光滑律在 $z_0$ 轴上奇异，全局化需两段式预控制。

### 1.3 时变非线性惯量柔性航天器（四阶全局 HOFA）
- **来源**：`J2022_018`（S4，T. Zhao & G.-R. Duan, *Sci. China Inf. Sci.* 2022, p.1–8）
- **原始动力学形式**（考虑液体晃动与燃料消耗导致的时变非线性转动惯量 $I(\theta,\dot\theta,t)$ 及太阳翼柔性模态 $q$）：
  $$I(\theta,\dot\theta,t)\ddot\theta + b\ddot q = u, \qquad \ddot q + 2\xi\Lambda\dot q + \Lambda^2 q + b\ddot\theta = 0.$$
- **HOFAS 转化形式**：在工程能控条件 $\Delta(\theta,\dot\theta,t)\triangleq I(\theta,\dot\theta,t)-b^2\neq 0$（Assumption 2）下，通过线性状态变换 $x_1=-\frac{b\Lambda}{2\xi}\theta+\frac{\Lambda(4\xi^2-1)}{2\xi}q+b\dot\theta+\dot q$ 与变量消元，严格等价为**四阶全局 HOFA**：
  $$x_1^{(4)} = -\frac{2\Lambda\xi I(\theta,\dot\theta,t)}{\Delta(\theta,\dot\theta,t)}x_1^{(3)} - \frac{\Lambda^2 I(\theta,\dot\theta,t)}{\Delta(\theta,\dot\theta,t)}\ddot x_1 - \frac{b\Lambda^3}{2\xi\Delta(\theta,\dot\theta,t)}u,$$
  且 $x_1^{(0\sim 3)}$ 与 $(\theta,q,\dot\theta,\dot q)$ 之间由显式常系数线性矩阵一一映射（无需数值求高阶导）。
- **FAS 在该背景上的优势 `[E]`**：
  1. 传统 PD、滑模、反步法在惯量时变非线性情形下闭环仍为非线性且多仅局部有效；
  2. HOFA 直接全额抵消时变非线性惯量项，得到**四阶线性定常闭环**且可任意参数化配置全部 4 个特征值（同时镇定刚体姿态与抑制柔性振动）。
- **适用前提与局限边界 `[E]`**：原文假设柔性模态 $q,\dot q$ 可测（工程不可测时须加观测器）；要求 $b,\xi,\Lambda\neq 0$ 且 $\Delta(\theta,\dot\theta,t)\neq 0$。

### 1.4 轨姿一体化航天器与航天器交会（Twistor 二阶 HOFA / OD-FAS）
- **来源**：`J2025_111`（S4，D. Jin, J. Qiu, H. Gao et al., *IEEE TSMC:S* 2025, p.2–4）；`J2023_016`（S4，F. Zhang & G. Duan, *IEEE/CAA JAS* 2023 综述）；`odfas_2026_part1` §1.1.1（Primary / S5）
- **原始动力学形式**（Twistor $B_{BD}=p_{BD}+\varepsilon\Pi_{BD}r^B_{BD}\in\mathbb{D}_v$ 仅 6 个独立自由度、无单位四元数约束，速度旋量 $V^B_{BD}=\omega^B_{BD}+\varepsilon(\dot r^B_{BD}+\omega^B_{BD}*r^B_{BD})$）：
  $$\dot B_{BD}=\frac{1}{4}(1+B_{BD})V^B_{BD}(1-B_{BD}), \quad \dot V^B_{BD}=M^{-1}(F^B_g+F^B_u-V^B_{BI}*MV^B_{BI})-\cdots$$
- **HOFAS 转化形式**：对运动学求导并利用对偶矩阵乘法算子 $D=[1+B_{BD}][1-B_{BD}]^\vee\in\mathbb{R}^{8\times 8}$（可逆），直接转化为**无约束二阶全驱系统**：
  $$\ddot B_{BD} = \frac{1}{4}DM^{-1}F^B_u + f_{\text{ao}}(B_{BD},\dot B_{BD},V^B_{BI},V^D_{DI}).$$
- **FAS 在该背景上的优势 `[E]`**：
  1. 传统分离式姿轨控制忽略强耦合，在近距离交会对接、悬停绕飞、抓捕消旋等 SPO 任务中精度不足；
  2. 基于 Twistor 的 FOSS 模型虽可统一描述姿轨，但控制器推导繁复且闭环非线性；转为二阶 HOFA 后，**一步同时消除姿轨强耦合与引力梯度/科氏非线性**，得到期望线性定常闭环（结合 `J2026_040` 可进一步纳入柔性附件，结合 `odfas_2026_part1` 可在仅测相对位置时避免对非线性的过度线性化如 C-W 方程局限）。
- **适用前提与局限边界 `[E]`**：MRP/Twistor 在 $360^\circ$ 旋转处存在切换（需影子集防退绕，参见 `J2026_034` / `J2025_113`）；模型不确定性与空间摄动需配固定时间/扩张状态干扰观测器。

### 1.5 飞行器俯仰通道（二阶 OD-FAS 输出反馈）
- **来源**：`odfas_2026_part4` Ex. 4.1 & 5.1（Primary / S5，p.21–23）
- **原始动力学形式**（攻角 $\alpha$、俯仰角速率 $\omega_z$、升降舵偏角 $\delta_z$，仅测输出 $y=\alpha$）：
  $$\dot\alpha = \omega_z - \frac{1}{mV}(P\sin\alpha + qSc_y\alpha), \qquad \dot\omega_z = \frac{qSLm_\alpha}{J_z}\alpha + \frac{qSLm_\delta}{J_z}\delta_z + d, \qquad y=\alpha.$$
- **OD-FAS 转化形式**：通过微分同胚 $x=\alpha,\;\dot x=\omega_z-\frac{1}{mV}(P\sin\alpha+qSc_y\alpha)$，化为仅依赖输出 $y=x$ 的二阶线性参数化 OD-FAS：
  $$\ddot x = A_0 x + A_1(x)\dot x + Bu + d, \quad A_0=\frac{qSLm_\alpha}{J_z},\; A_1(x)=-\frac{1}{mV}(P\cos x+qSc_y),\; B=\frac{qSLm_\delta}{J_z}.$$
- **FAS 在该背景上的优势 `[E]`**：无需测量俯仰角速率 $\omega_z$，直接给出显式**一阶降阶动态输出反馈补偿器**（$\dot z=K_{21}y+K_{22}z,\; u_0=K_{11}y+K_{12}z$），解析配置闭环极点与观测器极点 $A_{o1}$，实现全局一致渐近镇定（GUA），避免传统高增益全阶观测器带来的阶次膨胀与噪声放大。

---

## 二、无人机与空中平台

### 2.1 6-DOF 欠驱动四旋翼（Quadrotor）——两条主流 FAS 路线

#### 路线 A：4–4–4–2 混阶 sub-FAS（整体消元，无内外环近似）
- **来源**：`J2026_127`（S4，L. Xu, X. Wang, G. Duan, *IEEE TAES* 2026, p.2–4）
- **原始动力学形式**（6-DOF 仅 4 输入 $[u_1,u_2,u_3,u_4]^\top$，位置 $(x,y,z)$ 与欧拉角 $(\phi,\theta,\psi)$）：
  $$\ddot x = u_1(\cos\psi\sin\theta\cos\phi+\sin\psi\sin\phi),\quad \ddot y = u_1(\sin\psi\sin\theta\cos\phi-\cos\psi\sin\phi),\quad \ddot z = u_1\cos\theta\cos\phi - g,$$
  $$\ddot\phi = \frac{I_y-I_z}{I_x}\dot\theta\dot\psi + \frac{l}{I_x}u_2,\quad \ddot\theta = \frac{I_z-I_x}{I_y}\dot\phi\dot\psi + \frac{l}{I_y}u_3,\quad \ddot\psi = \frac{I_x-I_y}{I_z}\dot\theta\dot\phi + \frac{l}{I_z}u_4.$$
- **sub-FAS 转化形式**：由位置三式显式反解 $u_1=\Delta_2,\;\phi=\arcsin(\Delta_1/\Delta_2),\;\theta=\arctan(\Delta_4/\Delta_5)$（$\Delta_5=\ddot z+g$），二次求导代入姿态方程，以 $q=[x,y,z,\psi]^\top$、扩展输入 $\tau=[u_1',u_2,u_3,u_4]^\top$（$u_1'=\dot u_1^2+u_1\ddot u_1$）构成**混阶 $\mu=(4,4,4,2)$ 的连续/离散 sub-FAS**：
  $$M(\cdot)\begin{bmatrix}x^{(4)} \\ y^{(4)} \\ z^{(4)} \\ \ddot\psi\end{bmatrix} = f_{1\sim 4}(\cdot) + b\tau, \qquad \det M = \frac{\Delta_5^2+\Delta_4^2}{\Delta_2^2\Delta_3\Delta_5\Delta_6}\neq 0.$$
- **奇异集 / 可行集**：物理升力与姿态可行集 $\mathcal{Q}=\{q^{(0\sim\mu-1)}\in\mathbb{R}^{14} \mid \ddot z>-g,\; |\psi|<\pi\}$（等价于 $|\theta|<\pi/2,\; |\phi|<\pi/2$）。

#### 路线 B：$SO(3)$ 通道化 HOFA + ADRC（避免欧拉角奇异与冗余子系统）
- **来源**：`J2026_003`（S4，Aqeel-Ur-Rehman & C. Cai, *Aerospace Science and Technology* 2026, p.2–4）
- **原始与 HOFA 形式**：采用旋转矩阵 $Q=[q_{ij}]\in SO(3)$，$\ddot p = g_v + \frac{1}{M}Qf_T + \Delta_p$，$\dot Q=Q\Omega_\times$，$I\dot\Omega=-\Omega\times(I\Omega)+\tau+\Delta_\tau$。归一化输入 $u_1=u_T/M,\; u_2=[\tau_1/I_1,\tau_2/I_2]^\top,\; u_3=\tau_3/I_3$：
  - **高度二阶通道**：$\ddot p_z = -g + q_{33}u_1 + \delta_z$，取 $u_1=\frac{1}{q_{33}}(g-A_z\zeta_z+v_1)$（要求 $q_{33}>0$）；
  - **水平四阶通道**：对 $\ddot p_{xy}=u_1 q_{[13,23]}+\Delta_{xy}$ 求二阶导直接显式出现滚转-俯仰力矩 $u_2$：
    $$p_{xy}^{(4)} = f_{xy}(Q,\Omega,u_1,\dot u_1,\ddot u_1) + u_1 G(Q)u_2 + d_{xy}(t).$$
- **FAS 在四旋翼上的核心优势 `[E]`**：
  1. 打破传统内外环级联（需假设姿态环远快于位置环、在强风扰下耦合恶化）与反步法重复求导难题；
  2. 将强耦合欠驱动 6-DOF 飞行器解耦为线性定常子通道，使得预测控制（MPC）的非线性规划退化为**线性二次规划**（`J2026_127`），或与 ESO/ADRC 统一协调抑制集总气动/地面效应干扰（`J2026_003`）。
- **适用前提与局限边界 `[E]`**：欠驱动四旋翼的 4 阶模型需要参考轨迹 $p_d(t)$ 满足 $C^4$ 光滑，且存在非零推力与姿态角约束（$\ddot z>-g$ / $q_{33}>0$）；高阶变换会引入模型失配敏感性（`J2026_127` Remark 1 明确指出需结合 ISMC/ESO 处理）。

### 2.2 无人直升机（6-DOF Helicopter）编队与容错
- **来源**：`J2024_042`（S4，Y. Lu, K. Zhang, B. Jiang, *IEEE TCAS-I* 2024, p.2–4）；`J2024_061`（S4，Q. Miao, K. Zhang, B. Jiang, *AST* 2024, p.2–3）
- **原始与 HOFA 形式**：以主旋翼总距 $\delta_{\text{col}}$、纵向/横向周期变距 $\delta_{\text{lon}},\delta_{\text{lat}}$ 与尾桨总距 $\delta_{\text{ped}}$ 为 4 路输入，分别化为**位置外环二阶 HOFA** 与 **姿态内环二阶 HOFA**：
  $$\ddot P_i = U_{1i} + f_{1i} + D_{1i}, \qquad \ddot\Theta_i = G_i U_{2i} + f_{2i} + D_{2i}, \quad G_i = \Psi_i(\Theta_i)B_i.$$
- **可行条件**：$|\theta_i(t)|<\pi/2,\; |\phi_i(t)|<\pi/2$ 保证 $\Psi_i(\Theta_i)$ 与 $G_i$ 非奇异。
- **FAS 在该背景上的优势 `[E]`**：
  1. 直接消除主旋翼与尾桨之间的强轴间耦合与离轴响应，**不需要反步法的虚拟控制量也不需要传统滑模面**，计算复杂度显著降低（`J2024_042`）；
  2. 将 FAS 与增量非线性动态逆（INDI）结合形成 **增量全驱方法（IFASA）**（`J2024_061`）：用上一采样步的机载传感器实测状态替代精确气动/挥舞/斜盘模型进行非线性抵消，克服标准 FAS 对精确模型的依赖与观测器收敛前的瞬态失真。

### 2.3 全驱/过驱动无人机、空中机械臂与 PVTOL
- **代表来源**：`J2026_173`（S4，Y. Zhu, G. Duan et al., *IEEE/ASME TMech* 2026 — 双舵机全驱四旋翼 FAQts）；`J2025_043`（S4，Z. Li, H. Gao et al., *IEEE/ASME TMech* 2025 — 推力矢量空中机械臂 Quad3DVAM）；`J2024_027`（S4，L. Chen et al., *IEEE TRO* 2024 — 共轴双桨无人机）；`ucfas_2025_part3`（Primary / S5 — PVTOL 的 UC-FAS 模型）
- **核心特征与 FAS 优势 `[E]`**：
  - **硬件物理全驱/过驱动（FAQts / Quad3DVAM）**：通过 4 旋翼 + 2 舵机对角同步倾转（FAQts 仅增重 5.8%）或双轴倾转四旋翼（Quad3DVAM）实现 6-DOF 推力与力矩物理全驱 $m\dot v_e=R_e^b F^b-G$，直接套用二阶 HOFA + 固定时间干扰观测器，实现非零姿态悬停与抗侧风（实验中位置精度 $<1\text{ cm}$、姿态精度 $<1^\circ$），极大扩展空中机械臂作业空间；
  - **PVTOL 平面垂直起降机（`ucfas_2025_part3` Model 2）**：$\ddot q_1=-F_1\sin\gamma+\varepsilon F_2\cos\gamma,\;\ddot q_2=F_1\cos\gamma+\varepsilon F_2\sin\gamma-1,\;\ddot\gamma=F_2$（带非最小相位耦合 $\varepsilon$），无法化为单一 FAS，但归入**单向连接全驱系统（UC-FAS）**，可统一得到两个独立线性定常闭环并显式刻画 RoEA。

---

## 三、机械臂与精密运动平台

### 3.1 刚性/柔性关节机械臂（二阶 / 四阶 / 五阶全局 HOFA）
- **来源**：`ijss_2021_part2` Ex. 2（Primary / S5，*IJSS* 2021, p.12–13）；`J2025_087`（S4，H. Jiang, C. Hua et al., *IEEE TIE* 2025, p.2–3）
- **原始动力学形式**：
  - 单连杆弹性关节（含电机转矩动态，`ijss_2021_part2`）：
    $$J_1\ddot q_1 + D_1(\dot q_1)\dot q_1 + k(q_1-q_2)=d_1,\quad J_2\ddot q_2 + D_2\dot q_2 + k(q_2-q_1)=\tau+d_2,\quad \dot\tau=\phi(\tau)+u+d_3.$$
  - $n$-DOF 柔性关节机械臂（`J2025_087`）：
    $$M_o(q)\ddot q + C_o(q,\dot q)\dot q + G_o(q) + F_d(q,\dot q,\ddot q) = Z(\vartheta-q), \qquad S\ddot\vartheta + Z(\vartheta-q) = \tau.$$
- **HOFAS 转化形式**：
  - 从连杆方程直接显式消去电机侧转角 $q_2$（或 $\vartheta=Z^{-1}(M_o\ddot q+C_o\dot q+Zq+G_o+F_d)$），两次求导代入电机侧方程，化为**四阶全局全驱准线性模型**（计入电机电压动态则为**五阶**）：
    $$J_1 J_2 q_1^{(4)} + \sum_{i=1}^{3} c_i(q_1^{(1\sim 3)}) q_1^{(i)} = k\tau + \hat d, \qquad J_1 J_2 q_1^{(5)} + \sum_{i=1}^{4} a_i(q_1^{(1\sim 4)}) q_1^{(i)} - k\phi(\tau) = ku + k\dot d.$$
- **FAS 在该背景上的优势 `[E]`**：
  1. 柔性关节机械臂在状态空间中需 4 步甚至 5 步反步递推，面临严重的虚拟控制“微分爆炸”与计算膨胀；
  2. 直接以物理连杆角 $q$ 为基本状态消元成四阶/五阶 HOFA 后，**完全免除反步递推与虚拟控制器**，直接设计固定/预定时间或复合模糊自适应控制律并任意配置特征结构（`J2025_087`、`tcyb_2024_overview` §IX.C）。
- **适用前提与局限边界 `[E]`**：柔性刚度矩阵 $Z$（或 $k$）必须非奇异；高阶导数 $q^{(2)},q^{(3)}$ 在传感器噪声下难以直接数值微分，实际常需结合高增益/扩张状态观测器或奇异摄动降阶（见 7.1 节）。

### 3.2 水下双连杆耦合机械臂（二阶 OD-FAS 输出反馈）
- **来源**：`odfas_2026_part4` Ex. 4.2（Primary / S5，p.24–25）
- **原始与 OD-FAS 形式**（$q=[q_1,q_2]^\top$，惯量阵 $M(q_2)$ 与姿态依赖水动力阻尼阵 $C(q_2)$ 仅依赖输出 $q_2$）：
  $$M(q_2)\ddot q + C(q_2)\dot q + G(q) = \tau, \qquad y = q,$$
  其中 $M_{11}=J_1+J_2+2m_2L_1L_2\cos q_2,\; M_{12}=M_{21}=J_2+m_2L_1L_2\cos q_2,\; M_{22}=J_2$。在惯量条件 $J_1 J_2>m_2^2L_1^2L_2^2,\; J_1+J_2>2m_2L_1L_2$ 下，$M(q_2)$ 一致正定有界，属于标准二阶 OD-FAS。
- **FAS 在该背景上的优势 `[E]`**：仅测关节角度 $q$（无需角速度 $\dot q$），利用 $M(q_2),C(q_2)$ 仅依赖输出的结构直接构造降阶输出反馈动态补偿器（Theorem 4.3），避免了传统机器人输出反馈中复杂的非线性全阶观测器与高增益调参。

### 3.3 自由漂浮空间机械臂（FFSM）与双直线电机龙门平台（DLMDGS）
- **自由漂浮空间机械臂**（`J2024_057`，S4，G. Tian, G. Duan et al., *IEEE TAES* 2024, p.2–3）：由微重力线动量守恒消除基座线速度后，基座姿态与机械臂关节构成自然二阶全驱拉格朗日模型 $H(q)\ddot q + C(q,\dot q)\dot q = \tau + d$。相比一阶状态空间降阶法（易引入病态矩阵并丢失物理惯量含义），直接保留二阶全驱结构结合非线性干扰观测器（NDO）与梯度参数优化，兼顾关节角/力矩约束与低计算复杂度。
- **双直线电机龙门平台 DLMDGS**（`J2026_035`，S5，S. Jia, J. Qiu, H. Gao et al., *Automatica* 2026, p.2–3）：
  - **原始与全局任务坐标系（GTCF）二阶全驱形式**（$q=[x,y,\rho]^\top$ 为 $X/Y$ 平移与横梁偏转角，经可逆雅可比 $J$ 映至轮廓坐标 $q_r=[r_c,r_m,\rho]^\top$）：
    $$M_r\ddot q_r + C_r\dot q_r + B_r\dot q_r + A_r S_f(\dot q) + K_r q = T_{mr}u + d_r.$$
  - **FAS 优势 `[E]`**：直接保留二阶物理全驱特性（避免一阶状态空间破坏固有全驱性），配合**固定时间干扰观测器**补偿摩擦与电磁非线性，无需复杂神经网络即实现高速高精轮廓跟踪，且显著放松标准 FAS 对精确模型的依赖。

---

## 四、欠驱动机械系统

### 4.1 倒立摆与输入失效耦合倒立摆（sub-FAS 与精确 RoEA）
- **单倒立摆精确 RoEA 基准**（`fasta_2026_roea` Ex. 1 & 3，Primary / S5，p.2–6）：
  $$\ddot\theta = \sin\theta + u\cos\theta, \qquad \mathbb{F}=\{|\theta|<\pi/2\}.$$
  令 $u=-\frac{1}{\cos\theta}(a_1\dot\theta+a_0\theta+\sin\theta)$（如 $a_0=2,a_1=3$，极点 $-1,-2$），线性闭环解析解 $\theta(t)=(2-e^{-t})e^{-t}\theta_0+(1-e^{-t})e^{-t}\dot\theta_0$，由此通过有限驻点法**精确刻画**不越过 $|\theta|=\pi/2$ 的完整 RoEA $\mathcal{R}=\mathcal{R}_1\cap\mathcal{R}_2$。
- **三耦合倒立摆（CIPS）单通道完全失效**（`J2026_020`，S4，G. Duan et al., *Sci. China Inf. Sci.* 2026, p.2–5）：
  $$\ddot\theta_1=\frac{g}{l}\sin\theta_1+\frac{k_1 a^2}{m_1 l^2}(\sin\theta_2\cos\theta_2-\sin\theta_1\cos\theta_1)+u_1,\quad \ddot\theta_2=\cdots+u_2,\quad \ddot\theta_3=\cdots+u_3.$$
  当执行器 $u_1\equiv 0$（或 $u_2\equiv 0$）**完全失效**时，系统从全驱退化为欠驱动；利用弹簧耦合项反解 $\theta_2=\frac{1}{2}\arcsin\big(\frac{2m_1l^2}{k_1a^2}(\ddot\theta_1-\frac{g}{l}\sin\theta_1)+\sin 2\theta_1\big)$，化为四阶+二阶混阶 sub-FAS（可行条件 $|\frac{2m_1l^2}{k_1a^2}(\ddot\theta_1-\frac{g}{l}\sin\theta_1)+\sin 2\theta_1|<1$），仅凭剩余两个输入即可在显式 RoEA 内指数镇定全部三根倒立摆。

### 4.2 惯性轮摆（Inertia Wheel Pendulum, IWP）（四阶 sub-FAS）
- **来源**：`ijss_2024_underactuated4` Ex. 5.1（Primary / S5，*IJSS* 2024, p.14–15）；`odfas_2026_part1` §1.1.3（Primary / S5）
- **原始动力学形式**（摆角 $|\theta|<\pi/2$，惯性轮转角 $x$，驱动力矩 $\tau$，$b_2>b_1>0$）：
  $$\ddot\theta = M\sin\theta - b_1\tau, \qquad \ddot x = -M\sin\theta + b_2\tau.$$
- **sub-FAS 转化形式**：引入无输入线性组合基本状态 $y = b_2\theta + b_1 x$ 与虚拟输入 $u = M\sin\theta - b_1\tau$，化为串联型 $\ddot\theta=u,\;\ddot y=c\sin\theta$（$c=M(b_2-b_1)>0$）。在可行条件 $|\ddot y|<c$ 下反解 $\sin\theta=\ddot y/c,\;\cos\theta=\sqrt{c^2-\ddot y^2}/c,\;\dot\theta=y^{(3)}/\sqrt{c^2-\ddot y^2}$，二次求导得**四阶 sub-FAS**：
  $$y^{(4)} = -\frac{\ddot y\,(y^{(3)})^2}{c^2-\ddot y^2} + \sqrt{c^2-\ddot y^2}\,u.$$
- **FAS 在该背景上的优势 `[E]`**：通过显式微分同胚 $y^{(0\sim 3)}\leftrightarrow(\theta,\dot\theta,x,\dot x)$，直接得到线性定常四阶闭环 $y^{(4)}+\sum_{i=0}^3 a_i y^{(i)}=0$，绕开传统能量整形/IDA-PBC 求解偏微分方程（PDE）的困难，并能统一纳入 `ijss_2024_underactuated4` 四类欠驱动系统框架。

### 4.3 桥式吊车（单摆 / 双摆与全状态受限控制）
- **双摆桥式吊车（From Underactuated to FAS）**（`J2025_020`，S4，Y. Gao, Z. Zhang, Y. Wu et al., *IEEE TIE* 2025, p.2–7）：
  - **原始动力学**（台车位移 $x$，吊钩摆角 $\theta_1$，负载摆角 $\theta_2$，空气阻尼 $\omega_1,\omega_2$）：
    $$(M+m_1+m_2)\ddot x + (m_1+m_2)l_1\cos\theta_1\ddot\theta_1 + m_2 l_2\cos\theta_2\ddot\theta_2 - (m_1+m_2)l_1\sin\theta_1\dot\theta_1^2 - m_2 l_2\sin\theta_2\dot\theta_2^2 = u,$$
    另耦合两条无驱动二阶摆角方程（$M_{21}\ddot q_a+M_{22}\ddot q_u+C_{22}\dot q_u+G_2=-D\dot q_u$）。
  - **FAS 转化形式**：构造复合全驱变量 $\lambda = k\big((m_1+m_2)l_1\sin\theta_1+m_2l_2\sin\theta_2\big)$（$k=(M+m_1+m_2)^{-1}$）与 $S=x+\lambda-S_d$，将高度耦合的 3-DOF 欠驱动双摆吊车化为极其简洁的**二阶线性全驱形式**：
    $$\ddot S = \tau, \qquad \tau = ku - \ddot S_d.$$
  - **可行条件与仿真参数**：$|\theta_i|<\pi/2$；$M=50\text{ kg}, m_1=10\text{ kg}, m_2=100\text{ kg}, l_1=5\text{ m}, l_2=2\text{ m}, p_d=5\text{ m}$（强扰动下约 5 s 内消摆定位）。
  - **FAS 优势 `[E]`**：无需线性化小角近似、无需对复杂未驱动动力学求高阶导，控制律结构极其简洁，同时以未驱动能量 Lyapunov 函数严格证明 $x\to p_d,\;\theta_1,\theta_2\to 0$。
- **全状态受限吊车（无反步复合变量法）**（`J2026_144`，S5，Z.-C. Zhang, Y. Gao, Y.-Q. Wu, G.-R. Duan, *Automatica* 2026, p.2–3）：针对高阶全驱系统 $x^{(n)}=f(x^{(0\sim n-1)},t)+g(\cdot)u+d(t)$（允许库仑摩擦等不连续扰动，Filippov 解），对比传统 BLF 与非线性映射（NM）反步法（存在严重“微分爆炸”与虚拟控制界难以计算的可行性条件），构造两个复合辅助变量直接实现**无反步递推的全状态幅值约束** $|x^{(i)}|<k_{a(i+1)}$。

### 4.4 多弹簧-质量级联系统（$2r$ 阶全局 HOFA）
- **来源**：`ijss_2021_part7` Ex. 2.5 & 2.6（Primary / S5，*IJSS* 2021, p.9–10）
- **原始与 HOFA 形式**：$r$ 个质量块串联（仅末端受控 $u$），$m_i\ddot x_i + c_i(\dot x_i)+k_i(x_i-x_{i-1})=k_{i+1}(x_{i+1}-x_i)$，属于二阶严反馈系统；逐级变量消元直接等价为 $2r$ 阶全局 HOFA：$x_1^{(2r)}=\alpha_a(x_1^{(0\sim 2r-1)})+\beta_a u$（$\beta_a\neq 0$）。用于阐明“物理定律导出二阶基本方程 → 变量消元得高阶全驱模型（而非变量增广为一阶状态空间）”的建模哲学。

---

## 五、水面/水下无人艇与船舶

### 5.1 欠驱动水面船舶速度与位姿镇定（广义链式 sub-FAS）
- **来源**：`scis_2024_chained1` §5.2（Primary / S5，*SCIS* 2024, p.17–19）；`scis_2024_chained2` §6（Primary / S5，*SCIS* 2024, p.17–19）；`J2025_027`（S4，Z.-C. Zhang, G.-R. Duan, Y.-Q. Wu, *IEEE TCYB* 2025, p.2–3）
- **原始动力学形式**（纵荡 $v_x$、艏摇 $\omega$、无直接侧推的横荡 $v_y$，控制为纵推力 $\tau_x$ 与转艏力矩 $\tau_\omega$）：
  $$m_x\dot v_x = m_y v_y\omega - \sum_{j=1}^3 d_{0j}|v_x|^{j-1}v_x + \tau_x,\quad m_\omega\dot\omega = (m_x-m_y)v_x v_y - \sum_{j=1}^3 d_{1j}|\omega|^{j-1}\omega + \tau_\omega,\quad m_y\dot v_y = -m_x v_x\omega - \sum_{j=1}^3 d_{2j}|v_y|^{j-1}v_y.$$
- **广义链式与 FAS 转化形式**：动量变换 $(x_0,x_1,x_2)=(m_x v_x,m_\omega\omega,m_y v_y)$ 化为广义链式系统 $\dot x_0=u_0,\;\dot x_1=u,\;\dot x_2=x_2\hat\phi(x_2)+x_0 x_1\hat\psi(x_2)$（$\hat\psi=-1/m_\omega$）：
  - **Part 1 不连续缩放**：$z_1=x_2/x_0,\; z_2=x_1$（$x_0(0)\neq 0$ 且 $u_0=-\beta x_0$），化为二阶严反馈/全驱模型直接指数镇定；
  - **Part 2 连续控制器**：引入衰减因子 $\sigma_0(t)=c_2 e^{-\beta t}$ 令 $z_1=x_2/\sigma_0$，化为带指数衰减扰动 $\Delta f$ 的“几乎严反馈/全驱”模型，实现**连续控制器一致全局指数（UGE）镇定**；
  - **分段平滑延拓（`J2025_027`）**：对于初值落入奇异集需先由预控制器 $u_1(t)$ 推入可行集再切至 FAS 律 $u_2(t)$ 的情形，插入过渡段 $u_{12}(t)$ 消除切换时刻 $t_f$ 的控制跳变，实现**全局连续/光滑切换镇定**。
- **代表仿真参数**：Bis 标度船模 $m_x=1.1274,\; m_y=1.8902,\; m_\omega=0.1278$；阻尼 $d_{01}=0.0358, d_{11}=0.0308, d_{21}=0.1183$（$d_{i2}=0.5d_{i1}, d_{i3}=0.25d_{i1}$）；初值 $v_x(0)=5, v_y(0)=1, \omega(0)=\pm 0.5$。
- **FAS 优势 `[E]`**：打破非完整/欠驱动船舶无光滑时不变反馈律的 Brockett 障碍；相比传统 Lyapunov 直接法（调参极繁琐），FAS 将控制律转化为显式线性特征结构配置，并可自然推广至时变与时滞情形（`tcyb_2024_overview` §X.A）。

### 5.2 气垫船与平面水下航行器
- **气垫船速度系统**（`tcyb_2023_subfas` Ex. 2，Primary / S5）：$\dot s_1=s_2 r+f_c,\;\dot s_2=-s_1 r,\;\dot r=\tau_c$，经 $(x,y,z)=(s_1,-r,s_2)$ 严格等价于 Brockett 第一反例，适用 1.2 节的几乎全局指数亚镇定（可行集 $s_1^2+r^2\neq 0$）。
- **平面欠驱动水下航行器**（`ucfas_2025_part3` Model 3，Primary / S5）：$\ddot x_1=u_1,\;\ddot x_2=u_2,\;\ddot\theta=u_1\cos\theta+u_2\sin\theta$，统一归入单向连接全驱系统（UC-FAS）进行亚镇定与 RoEA 刻画。

---

## 六、移动机器人、智能车辆与非完整/广义链式系统

### 6.1 Brockett 第二反例、两轮移动机器人与平面双旋翼（sub-FAS）
- **来源**：`jssc_2023_brockett2`（Primary / S5，*JSSC* 2023, p.1–6）
- **等价物理背景群（Forms 0–V 严格等价）**：
  - **Form 0（Brockett 第二反例）**：$\dot y_1=u_1,\;\dot y_2=u_2,\;\dot y_3=y_2 u_1-y_1 u_2$；
  - **Form I（两轮非完整移动小车 / 刀刃）**：$\dot x_1=v\cos\theta,\;\dot x_2=v\sin\theta,\;\dot\theta=w$；
  - **Form II（平面双旋翼）**：$\dot x_1=(v_1+v_2)\cos\theta,\;\dot x_2=(v_1+v_2)\sin\theta,\;\dot\theta=v_1-v_2$；
  - **Form V（非完整/Brockett 积分器）**：$\dot z_1=u_1,\;\dot z_2=u_2,\;\dot z_3=z_2 u_1$。
- **FAS 转化与核心优势 `[E]`**：
  1. 经典控制界因 Brockett 必要条件普遍采用复杂的时变反馈或高频切换滑模；
  2. 转为 sub-FAS 后，仅用**极简的连续时不变光滑状态反馈**即实现大范围指数亚镇定，其不可行补集（蒸发区）仅为**一个张角可通过闭环极点配置任意缩小的扇形域**；初值落入该极小扇形时只需极简预控制一步推入可行域。

### 6.2 多向量广义链式系统与不平路面轮式移动机器人（WMR）
- **多向量广义链式系统**（`scis_2025_chained3`，Primary / S5，*SCIS* 2025）：将单标量链式系统拓展到多输入多向量高阶情形（$z^{(n)}=\check f_n+\cdots$），转为 sub-SFS 再等价化为 sub-FAS，实现连续/不连续指数镇定。
- **不平路面差速轮式移动机器人 WMR**（`J2025_045`，S4，J. Qiang, C. Hua et al., *IEEE TCAS-I* 2025, p.2–3）：
  - **运动学（计入路面俯仰 $\phi_c$ 与滚转 $\gamma_c$ 引起的未知投影因子 $\alpha=\cos\phi_c,\;\beta=\cos\gamma_c/\cos\phi_c$）**：$\dot P_c=S(\theta_c)v_c$；
  - **直流电机驱动内环二阶全驱模型**：$\ddot v(t)=-\kappa_1 v(t)-\kappa_2\dot v(t)+\kappa_3 u(t)+f(t)$（$v=[v_R,v_L]^\top$，$u=[u_R,u_L]^\top$）；
  - **FAS 优势 `[E]`**：内环保留二阶全驱速度模型，结合固定时间广义变增益 ESO（VGESO）与实用预定时间（PPT）控制，在路面扰动下使速度跟踪误差在预定时间内收敛至任意设定精度且与初始观测误差无关。

---

## 七、电机、电力电子、微电网与柔性伺服

### 7.1 双惯量柔性伺服系统（四阶 HOFA + 奇异摄动降阶双二阶全驱）
- **来源**：`J2023_023`（S4，P. Li & G. Duan, *IEEE/ASME TMech* 2023, p.2–4）
- **原始动力学形式**（电机轴角 $\theta_m$、负载轴角 $\theta_L$、弹性轴刚度 $K_s$、电机输出力矩 $T_m=K_T i$）：
  $$J_L\ddot\theta_L + B_L\dot\theta_L + T_L = K_s(\theta_m-\theta_L), \qquad J_m\ddot\theta_m + B_m\dot\theta_m + K_s(\theta_m-\theta_L) = T_m.$$
- **HOFAS 转化形式（两种尺度路线）**：
  1. **直接消元四阶全局 HOFA**：消去 $\theta_m,\dot\theta_m,\ddot\theta_m$ 得
     $$\theta_L^{(4)} + \alpha_3\theta_L^{(3)} + \alpha_2\ddot\theta_L + \alpha_1\dot\theta_L = \frac{K_s}{J_m J_L}u - d_1,$$
     其中 $d_1=\frac{1}{J_m J_L}(J_m\ddot T_L+B_m\dot T_L+K_s T_L)$，可一步配置全部 4 个闭环极点；
  2. **奇异摄动（SP）降阶双二阶全驱**（针对高阶导数受测量噪声与离散误差放大的工程痛点）：令 $\tau_s=K_s(\theta_m-\theta_L),\; K_s=k_0/\varepsilon^2$，拆分为
     - **慢时标刚体二阶全驱**：$(J_m+J_L)\ddot\theta_L+(B_m+B_L)\dot\theta_L+T_L=u_s$（配 HOFA + 动态补偿器）；
     - **快时标谐振边界层二阶全驱**：$\eta_1''+\frac{\varepsilon B_m}{J_m}\eta_1'+\frac{k_0(J_m+J_L)}{J_m J_L}\eta_1=\frac{k_0}{J_m}u_f$（主动阻尼抑振）。
- **FAS 在该背景上的优势与诚实局限 `[E]`**：
  - 相比陷波滤波器（对谐振频率漂移极敏感）、SP-PID（三类参数试凑、缺性能映射）与模糊/神经网络（缺严格闭环稳定性保证、结构复杂），**HOFA+SP 同时实现了显式极点配置、谐振主动抑振、低阶易工程部署与严格鲁棒稳定证明**；
  - 该文 Remark 1 客观指出标准四阶 HOFA 的现实痛点：直接用于跟踪需 $\theta_d^{(4)}$ 与高阶测量微分，对噪声与模型不确定性敏感——**奇异摄动降阶 + 动态补偿器正是解决工业伺服落地的关键方案**。

### 7.2 直流微电网（带感性联络线的离散全驱建模与分布式预测控制）
- **来源**：`J2025_049`（S4，Y. Yu, G.-P. Liu, P. Shi et al., *IEEE TIE* 2025, p.2–5）；`tcyb_2024_overview` §IX.D.4（Primary / S5）
- **原始动力学形式**（多母线孤岛直流微电网，计入 RLC 滤波器、DC-DC 占空比 $d_{\text{duty},i}$、底层电压/电流双闭环 PI、下垂控制 $v_{o,i}^*=V_{ni}-R_{vi}i_{t,i}+\delta_i$，以及以往常被忽略的感性联络线 $L_{i i_k}\dot i_{l,i i_k}=-R_{i i_k}i_{l,i i_k}+v_{o,i_k}-v_{o,i}$）：
  $$C_{fi}\dot v_{o,i}=-R_{Li}^{-1}v_{o,i}+i_{t,i}+\sum_{j\in\mathcal{N}_i^p}i_{l,ij}, \quad L_{fi}\dot i_{t,i}=V_{\text{in}}d_{\text{duty},i}-v_{o,i}-R_{fi}i_{t,i}.$$
- **FAS 转化形式**：欧拉离散化得到完整物理层耦合状态方程后，验证 $C_i B_{ii}=b_{c,i}=L_{fi}^{-1}V_{\text{in},i}k_{P,ii}k_{P,iv}\neq 0$，经二次控制输入变换 $u_{r,i}(k)=b_{c,i}^{-1}(u_{ca,i}(k)+u_i(k))$，在保留全部真实电力网络耦合信息的前提下转化为极简的**离散全驱电流模型**：
  $$i_{t,i}(k+1) = i_{t,i}(k) + u_i(k).$$
- **FAS 在该背景上的优势 `[E]`**：
  1. 解决传统直流微电网建模的两难困境：完整电路多智能体模型虽精确但破坏分布式预测控制结构；把下垂层简化为常数 1 或独立一阶模型虽易设计却脱离物理电路层与电压-电流电气约束；
  2. FAS 模型**既保留了感性联络线与底层双闭环的真实物理耦合，又使信息层呈现极简全驱结构**，可直接开展分布式滚动优化预测二次控制，统一化解电压恢复（CVR）与均流（ACS）的固有矛盾。

### 7.3 直线开关磁阻电机（LSRM，离散二阶全驱与观测器协同设计）
- **来源**：`J2026_068`（S3，Y.-Y. Liu, L. Qiu et al., *IJSS* 2026, p.3–6）
- **原始与离散 HOFA 形式**：内环电流快速跟踪后，动子机械动力学为二阶全驱 $M\ddot x+\mu\dot x+f=F$；经二阶差分直接离散化为**离散时间二阶全驱模型**：
  $$x(k+1) = -A_{0\sim 1}x^{\lceil 0\sim 1\rceil}(k) + BF(k), \quad A_0=\frac{\mu T_s}{M}-2,\; A_1=1-\frac{\mu T_s}{M},\; B=\frac{T_s^2}{M}.$$
- **FAS 在该背景上的优势 `[E]`**：避免将二阶机械方程增广为一阶状态空间时产生的**病态系数矩阵、增益对参数高敏感度与稳态误差放大**；直接在二阶全驱框架下同步构造结构一致的预测观测器与两自由度参数化特征结构配置控制器，显著提升数值鲁棒性与跟踪精度。

---

## 八、工业过程、气动执行器与车辆主动悬架

### 8.1 1/4 车辆主动悬架系统（输入死区 + 仿生参考模型二阶全驱）
- **来源**：`J2025_022`（S4，M. Zhang, N. Sun et al., *IEEE TIE* 2025, p.2–3）
- **原始动力学形式**（簧载质量 $m_s$、非簧载质量 $m_u$、路面激励 $z_r$、伺服电机输入死区 $Z(u(t))=u(t)+\Delta u(t)$）：
  $$m_s\ddot z_s = -F_s(z_s,z_u)-F_d(\dot z_s,\dot z_u)+Z(u(t)), \quad m_u\ddot z_u = F_s+F_d-F_t(z_u,z_r)-F_b(\dot z_u,\dot z_r)-Z(u(t)).$$
- **FAS 转化形式**：以悬架动行程 $z_p=z_s-z_u$ 为基本状态，两式相减直接化为二阶全驱模型：
  $$\ddot z_p = -\frac{m_u+m_s}{m_s m_u}(k_s z_p + k_d\dot z_p) + \frac{1}{m_u}(F_t+F_b) + \frac{m_u+m_s}{m_s m_u}\big(u(t)+\Delta u(t)\big).$$
- **FAS 在该背景上的优势 `[E]`**：无需线性化即可获得简洁通用控制框架，克服传统主动悬架难以构造 Lyapunov 函数的瓶颈；结合 RBFNN 处理簧载质量变化与输入死区，并通过仿生参考模型选择性保留有益非线性以显著节省控制能耗（并经硬件台架实验验证）。

### 8.2 2-DOF 气动肌肉并联机构（滞回补偿 + 实用预定时间全驱）
- **来源**：`J2026_009`（S4，Y. Cao, C. Hua et al., *IEEE TSMC:S* 2026, p.2–3）
- **原始与 FAS 形式**（两对拮抗气动肌肉 PMA 驱动 $X/Y$ 偏转角 $\theta_1,\theta_2$，含广义 Prandtl–Ishlinskii 滞回 $\omega_i(u_i)$ 与未知角速度）：
  $$J_i\ddot\theta_i(t) + \zeta_i\dot\theta_i(t) = b_i\omega_i(u_i(t)) + v_i(t), \quad i=1,2.$$
  串联逆 GPI 滞回补偿器后形成 2-DOF 气动并联全驱系统（PPFAS），配无切换实用预定时间扩张状态观测器（PPTESO）估计角速度与集总扰动。
- **FAS 在该背景上的优势 `[E]`**：相比基于反步法的实用预定时间控制，PPTFAC 保留二阶全驱形式、**彻底避免虚拟控制器反复求导造成的微分爆炸**，且不依赖切换型时间缩放函数，在预定时间 $T$ 之后仍平滑连续运行（含实验验证）。

---

## 九、主动容错、混合脉冲/切换 sub-FAS 与经典非线性基准

### 9.1 未知非线性 HOFAS 主动容错控制框架（AFTC）
- **来源**：`J2023_011`（S5，M. Cai, X. He, D. Zhou, *Automatica* 2023, p.2–3）；续作 `J2026_005`（S5，*Automatica* 2026 多故障容错）
- **模型形式**（$F_o,G_o,K_o$ 均未知光滑函数、未建模动态 $\xi(t)$、仅测输出 $\tilde y=H_o(x_o)$）：
  $$x_o^{(n)}(t) = F_o(x_o^{(0\sim n-1)},\xi) + G_o(x_o^{(0\sim n-1)},\xi)u(t) + K_o(x_o^{(0\sim n-1)},\xi)d(t), \quad \tilde y = H_o(x_o).$$
  在相对阶 $n$ 条件下通过李导数坐标变换化为规范未知 HOFAS（$\tilde y=x$）。
- **核心价值与局限揭示 `[E]`**：明确点出早期理想 HOFAS 对**精确模型与全维状态可测**的强依赖——一旦发生执行器/传感器/部件故障或参数未知，非线性抵消失效将破坏预设计线性闭环；通过自适应观测器 + 动态数据建模重构故障与不确定性，首次建立面向未知非线性 HOFAS 的主动容错安全框架。

### 9.2 混合脉冲控制全局镇定 sub-FAS（突破初值 RoEA 限制）
- **来源**：`J2025_064`（S3，Q. Huang, J. Sun, M. Zhao, *ISA Transactions* 2025, p.2–3）
- **模型形式**：在 sub-FAS $\dot x_j=x_{j+1}+u_{1j}\;(j<m),\; \dot x_m=f(x_{1\sim m},t)+B(x_{1\sim m},t)u_2+u_{1m}$ 上，令重置集 $\mathcal{M}=\mathbb{S}\setminus\{0\}$；轨迹远离 $\mathbb{S}$ 时运行标准 HOFA 连续控制器 $u_2$，在每次触及 $\mathcal{M}$ 的瞬间 $\tau_k$ 施加状态依赖脉冲 $u_{1j}=\sum_k C_{0\sim m-1}^{k,j}x_{1\sim m}\delta(t-\tau_k)$ 将状态跃迁出奇异集。
- **核心价值与边界 `[E]`**：对比纯连续 sub-FAS 亚镇定（需初值位于 RoEA）及单次初值预控制切换（仅允许初始时刻在奇异集），该方案允许任意初值与任意时刻轨迹触及奇异集而实现**全局指数镇定**；但原文客观指出，状态依赖脉冲执行器在工程实现上更复杂，且引入脉冲扰动效应使分析变复杂。

### 9.3 Lorenz 混沌系统与 Isidori / Khalil 非线性基准
- **Lorenz 系统（内可行集三阶 sub-FAS）**（`fasta_2026_roea` Ex. 2 & 4，Primary / S5，p.2–7）：
  $$\dot x=\sigma(y-x),\quad \dot y=rx-y-xz,\quad \dot z=xy-bz,$$
  经 $p=\frac{1}{2}x^2-\sigma z,\; u_y=rx-y-xz$ 化为三阶 sub-FAS $p^{(3)}=f(x,y,z)+\sigma(b-2\sigma)x\,u_y$，内可行条件 $x^2=\frac{2}{b-2\sigma}(bp+\dot p)>0$（标准参数 $b=8/3,\sigma=10,r=24.74$），是验证无拐点闭环响应精确 RoEA 的标杆三阶算例。
- **Isidori 8 态 3 输入非线性基准**（`ucfas_2025_part1` Ex. 4.1 & `part2` Ex. 3.1，Primary / S5）：无法化为单一 FAS，但可化为强/弱单向连接全驱系统（UC-FAS），用于演示内/外可行集交集 $\mathbb{F}^{\mathrm{in}}\cap\mathbb{F}^{\mathrm{ex}}$ 与三级自然递推亚镇定。

---

## 十、跨物理背景 FAS 核心优势与客观边界速查总表

| 物理背景 | 典型 FAS 分支 | 相比传统方法的核心优势 `[E]` | 客观前提与工程边界 `[E]` |
|---|---|---|---|
| **刚体/柔性航天器与轨姿一体** | 二阶/四阶 HOFA & sub-FAS、Twistor 二阶 HOFA | 保留牛顿-欧拉二阶物理结构；一步消除姿轨耦合与时变非线性惯量；任意配置线性闭环特征结构与解耦最优控制 | 欧拉角有 $|\phi|<\pi/2$ 奇异面；柔性模态/空间摄动需观测器；MRP/Twistor 需防 $360^\circ$ 退绕 |
| **四旋翼 / 无人直升机 / 空中机械臂** | 4–4–4–2 sub-FAS、$SO(3)$ HOFA-ADRC、IFASA、硬件全驱 FAQts | 打破传统内外环时间尺度分离与反步微分爆炸；使非线性 MPC 退化为线性 QP；IFASA 结合 INDI 降低模型依赖 | 欠驱动 4 阶模型要求参考轨迹 $C^4$ 且 $\ddot z>-g$（$q_{33}>0$）；高阶变换放大模型失配，须配 ESO/ISMC/INDI |
| **柔性关节 / 水下 / 空间机械臂与精密平台** | 二阶/四阶/五阶 HOFA、二阶 OD-FAS | 免除 4–5 步反步递推与虚拟控制求导；保留正定惯量阵物理意义避免一阶增广病态；OD-FAS 仅测位置实现降阶输出反馈 | 刚度阵须非奇异；高阶导数抗噪弱（需观测器或奇异摄动降阶）；精密跟踪须配固定时间干扰观测器 |
| **吊车 / 倒立摆 / 惯性轮摆 / 弹簧质量** | 复合变量二阶 FAS、四阶 sub-FAS、$2r$ 阶 HOFA | 无需小角线性化与 IDA-PBC 偏微分方程求解；复合变量大幅简化双摆吊车与全状态受限控制（无 BLF 微分爆炸）；精确刻画 RoEA 并在单通道完全失效下亚镇定 | 依赖摆角约束 $|\theta|<\pi/2$ 或 $|\ddot y|<c$；sub-FAS 亚镇定须初值位于 RoEA（全局化需预控制切换或脉冲） |
| **欠驱动船舶 / 气垫船 / 移动小车 / 链式系统** | 广义链式 sub-FAS、UC-FAS、平滑延拓切换 | 突破 Brockett 光滑镇定障碍：以连续/光滑时不变反馈实现大范围指数亚镇定（蒸发区可任意缩小）；支持时变与时滞推广 | 存在零测度奇异轴/极小扇形蒸发区；全局镇定需极简预控制器或平滑过渡段 $u_{12}(t)$ |
| **柔性伺服 / LSRM / 直流微电网** | 离散二阶全驱、HOFA + 奇异摄动、离散全驱电流模型 | 消除一阶增广病态矩阵；微电网在保留感性联络线物理耦合下获得极简分布式预测全驱模型；伺服 SP+HOFA 兼具抑振与低阶落地 | 需兼顾离散采样误差与高频谐振；直接高阶全驱受测量噪声限制，工业伺服宜走奇异摄动/动态补偿器路线 |
| **主动悬架 / 气动并联 / 主动容错** | 二阶 HOFA + 逆滞回/RBFNN/PPTESO、未知 HOFAS AFTC | 避免反步微分爆炸与难构 Lyapunov 函数；易于模块化叠加滞回逆补偿、死区 RBFNN、固定/预定时间 ESO 与容错重构 | 标准 FAS 依赖精确模型与全态可测；工程落地几乎均需“FAS 主框架 + 观测器/自适应/容错模块”复合架构 |
