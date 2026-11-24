# FAS 物理背景与仿真算例全量目录（36 篇一级权威库 + 二级 3–5 分高分期刊库）

> 本目录由 `scripts/build_physical_examples_catalog.py` 自动生成，版权安全（仅含结构化目录与元数据索引，不含整篇受版权保护全文）。
> 详细动力学方程、HOFAS/sub-FAS/UC-FAS/OD-FAS 具体转化形式、奇异集/可行集、仿真参数及各背景专属优势分析，见 `references/physical-examples-and-advantages.md`。

## 一、高分期刊库（Score 3–5）按物理背景分布统计

| 物理背景 / 基准类别 | Score 5 | Score 4 | Score 3 | 3–5 分合计 |
|---|---:|---:|---:|---:|
| 1. 航天器与空天飞行器（姿态 / 交会 / 轨姿一体 / 编队 / 高超声速） | 1 | 24 | 30 | **55** |
| 2. 无人机与空中平台（四旋翼 / 直升机 / 倾转旋翼 / 空中机械臂） | 0 | 18 | 17 | **35** |
| 3. 机械臂与精密运动平台（刚/柔性关节 / 绳驱 / 水下 / 龙门平台） | 1 | 7 | 10 | **18** |
| 4. 欠驱动机械系统（吊车 / 倒立摆 / 惯性轮摆 / TORA / 球杆 / Acrobot / 弹簧质量） | 1 | 10 | 2 | **13** |
| 5. 水面/水下无人艇与船舶（USV / AUV / 船舶 / 气垫船） | 0 | 1 | 4 | **5** |
| 6. 移动机器人、智能车辆与非完整/链式系统（Unicycle / Brockett / 广义链式 / 车队） | 6 | 6 | 4 | **16** |
| 7. 电机、电力电子、微电网与磁悬浮伺服（PMSM / LSRM / 微电网 / 磁悬浮 / 柔性伺服） | 0 | 9 | 4 | **13** |
| 8. 工业过程、液压/气动执行器与车辆主动悬架（CSTR / 气动 / 液压 / 悬架） | 0 | 6 | 6 | **12** |
| 9. 切换系统、脉冲/混合控制、主动容错与经典非线性基准（Switched / Impulsive / FTC / Lorenz / Isidori） | 2 | 31 | 23 | **56** |

## 二、36 篇 Duan 一级权威库 `Example` 与应用章节速查（覆盖 30 篇）

### `fasta_2026_roea` (4)
- `L171`: Example 1. Consider the following pendulum system
- `L223`: Example 2. Consider the Lorenz system [9]
- `L522`: Example 3. For the pendulum system (1), the function (20)
- `L660`: Example 4. Consider the RoEA (12) of Lorenz System (7)

### `ijss_2021_part1` (3)
- `L1108`: [Section] 4. Example z˙I = g (z) , (50)
- `L1110`: [Section] 4.1. Example 1 z˙II = f (z) + G (z) u, (51)
- `L1220`: [Section] 4.2. Example 2

### `ijss_2021_part2` (3)
- `L1153`: [Section] 4. Examples
- `L1155`: [Section] 4.1. Example 1. Cascade systems
- `L1242`: [Section] 4.2. Example 2. Under-actuated systems

### `ijss_2021_part3` (1)
- `L1753`: [Section] 6. An illustrative example

### `ijss_2021_part4` (2)
- `L1619`: [Section] 6. Illustrative example
- `L1780`: [Section] 6.3. Simulation results

### `ijss_2021_part5` (2)
- `L1220`: [Section] 7. An illustrative example
- `L1324`: [Section] 7.2. Simulation results

### `ijss_2021_part6` (4)
- `L593`: Example 2.2: Let us consider the disturbance
- `L1513`: [Section] 5. Illustrative example
- `L1837`: [Section] 5.2.3. Comparative simulation results
- `L2014`: [Section] 5.3.3. Simulation results

### `ijss_2021_part7` (11)
- `L810`: Example 2.4: Attitude system of a flying vehicle
- `L893`: Example 2.5: Multiple spring-mass systems
- `L956`: Example 2.6: Multiple spring-mass systems
- `L1212`: Example 3.4: Consider the following system
- `L1268`: Example 3.5: Multiple spring-mass systems
- `L1272`: Examples 2.5 and 2.6 that the systems (a) and (b) in
- `L1493`: Example 4.3: Consider the following system
- `L1521`: Example4.4: Consider a special type of linear systems
- `L1967`: [Section] 6. Examples
- `L1979`: Example 6.1: Consider the following nonlinear sys-
- `L2114`: Example 6.2: Consider the following nonlinear sys-

### `ijss_2022_part10` (1)
- `L1933`: Example 7.5: Consider a specific pseudo feed-

### `ijss_2022_part8` (2)
- `L1325`: [Section] 6. Spacecraft attitude control
- `L1522`: [Section] 6.3. Simulation results

### `ijss_2022_part9` (3)
- `L1807`: [Section] 7. Illustrative example
- `L2047`: [Section] 7.4. Simulation results
- `L2166`: [Section] 8. Conclusions simulations.

### `ijss_2024_underactuated4` (4)
- `L780`: Example 3.1: Consider the following class of systems:
- `L858`: Example 3.2: Consider the following system in the
- `L1180`: Example 4.1: Consider the following class of systems
- `L1579`: Example 5.1: Consider the inertia wheel pendulum,

### `jssc_2022_brockett1` (1)
- `L77`: [Section] 1.1 Spacecraft Control Background

### `jssc_2022_freq` (3)
- `L305`: Example 3.4 Consider the following controllable linear system[13]
- `L556`: Example 4.7 We reconsider Example 3.4. First, we notice that D′(s) in (15) is not
- `L737`: Example 5.2 Consider a discrete-time linear state-space system in the form of (32) with

### `jssc_2023_brockett2` (1)
- `L695`: [Section] 4.1 Simulation

### `odfas_2026_part1` (8)
- `L124`: [Section] 1.1.1. Spacecraft rendezvous control
- `L177`: [Section] 1.1.3. Inertial wheel pendulums
- `L498`: Example 2.1. Consider the following system
- `L668`: Example 2.2. Consider the system formed by
- `L830`: [Section] 3.1.2. An illustrative example
- `L1039`: [Section] 3.2. Spacecraft Rendezvous Using Only
- `L1246`: [Section] 3.3. Output Control of A Manipulator
- `L1620`: [Section] 4.3. A Benchmark Example

### `odfas_2026_part2` (4)
- `L627`: [Section] 2.3. Anillustrativeexample
- `L1288`: [Section] 3.3. Athree-degreeplanarmanipulator
- `L2256`: [Section] 6. Coupled-invertedpendulumswithinput
- `L2824`: [Section] 6.3. Simulation

### `odfas_2026_part4` (9)
- `L482`: Example 2.1. Consider the one-DOF system
- `L517`: Example 2.2. Consider the two-DOF nonlinear system:
- `L545`: Example 2.3. Consider the two-DOF nonlinear system:
- `L575`: Example 2.4. Consider the two-DOF nonlinear system:
- `L1262`: Example 4.1. Control of the Pitch Channel of a Flying Vehicle
- `L1405`: Example 4.2. Control of a 2-DOF coupled underwater manipulator
- `L1979`: Example 5.1. Control of the Pitch Channel of a Flying Vehicle (Continued)
- `L2887`: [Section] 8. Control of Marine Vehicles
- `L3417`: [Section] 8.5. Simulation

### `scis_2022_discdelay1` (2)
- `L893`: Example 1. Consider a system in the form of
- `L974`: Example 2. Consider the following FAS:

### `scis_2022_discdelay2` (2)
- `L694`: Example 1. Consider a system in the form of
- `L800`: Example 2. Consider the following discrete-time sub-FAS:

### `scis_2023_delay1` (10)
- `L378`: Example 1. Consider a strict feedback system in the form of (13) with state delays as follows:
- `L650`: Example 2. Consider the following system studied in [53]:
- `L781`: Example 3. Consider the following system in [54]:
- `L910`: Example 4. In [55], the following simple but important nonlinear system without delays is introduced:
- `L1004`: Example 5. Continuation of Example 1.
- `L1023`: Example 6. Continuation of Example 3.
- `L1121`: Example 7. Continuation of Example 2.
- `L1177`: Example 8. Continuation of Example 4.
- `L1436`: Example 9. Continuation of Example 6.
- `L1607`: Example 10. Continuation of Example 9.

### `scis_2023_delay2` (3)
- `L333`: Example 1. Consider the following system [45]:
- `L625`: Example 2. Let us continue with the system in Example 1.
- `L719`: Example 3. Let us continue with Example 2.

### `scis_2024_chained1` (1)
- `L1087`: [Section] 5.2 Application to ship control

### `scis_2024_chained2` (1)
- `L1224`: [Section] 6.3 Simulation results

### `tcyb_2023_robustdelay` (1)
- `L1236`: [Section] VII. TWO ILLUSTRATIVE EXAMPLES

### `tcyb_2023_subfas` (4)
- `L286`: Example 1: Consider a system in the following state-space
- `L376`: Example 2: Let us consider two practical backgrounds.
- `L721`: Example 3: In Example 1, the normal singularity condi-
- `L1244`: [Section] VI. ILLUSTRATIVE EXAMPLE

### `tcyb_2024_overview` (2)
- `L247`: [Section] IX. Applications
- `L2013`: [Section] IX. APPLICATIONS

### `ucfas_2025_part1` (2)
- `L580`: Example 4.1: Consider the following system with 8
- `L803`: Example 5.1: Consider the following system (Isidori,

### `ucfas_2025_part2` (3)
- `L1001`: [Section] 3.4. Demonstrating examples ||q6 + u1|| < ρ, (58)
- `L1003`: Example 3.1: Consider again the following system
- `L1154`: Example 3.2: Consider the following system (Isidori,

### `ucfas_2025_part3` (2)
- `L38`: [Section] III. Applications
- `L1153`: [Section] 5.3. Simulation

## 三、二级高分期刊库（Score 3–5）按背景分类索引

> 注：跨领域论文（如空间机械臂、切换容错飞行器）可在多个相关背景中同时出现；排序严格按分值降序（5 → 4 → 3），再按年份降序。

### 1. 航天器与空天飞行器（姿态 / 交会 / 轨姿一体 / 编队 / 高超声速）（共 55 篇）

- `[S5]` `J2022_022` (2022, *International Journal of Systems Science*): G.-R. Duan — High-order fully actuated system approaches: Part VIII. Optimal control with application in spacecraft attitude stabilisation | DOI: `10.1080/00207721.2021.1937750`
- `[S4]` `J2026_169` (2027, *Aerospace Science and Technology*): Q. Zheng, K. Sun, and J. Qiu — Twistor-based state-feedback tracking control for attitude-orbit integrated spacecraft: A fully actuated system approach | DOI: `10.1016/j.ast.2026.113611`
- `[S4]` `J2026_012` (2026, *IEEE Transactions on Industrial Electronics*): K.-X. Cui, D.-W. Zhang, and X.-Y. Xu — Discrete-Time Robust Adaptive Stabilization Control for A Type of Combined Spacecraft: A Fully Actuated System Approach | DOI: `10.1109/TIE.2026.3679723`
- `[S4]` `J2026_013` (2026, *IEEE Transactions on Industrial Electronics*): K.-X. Cui, D.-W. Zhang, and X.-Y. Xu — Discrete-Time Robust Adaptive Stabilization Control for A Type of Combined Spacecraft: A Fully Actuated System Approach | DOI: `10.1109/TIE.2026.3679723`
- `[S4]` `J2026_034` (2026, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): S. Jia, L. Yuan, J. Qiu, T. Wang, and M. Li — Anti-Unwinding Active Fault-Tolerant Attitude Tracking Control for Uncertain Spacecraft via Fully Actuated System Approach | DOI: `10.1109/TSMC.2026.3659255`
- `[S4]` `J2026_040` (2026, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): D. Jin, J. Qiu, W. Ji, and T. Wang — Attitude-Orbit Integrated Modeling and Control for Flexible Spacecraft Based on Twistors and Fully Actuated System Approach | DOI: `10.1109/TSMC.2025.3647684`
- `[S4]` `J2026_041` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): D. Jin, J. Qiu, W. Ji, and T. Wang — Integrated Attitude-Orbit Control for Spacecraft With Prescribed Performance via Fully Actuated System Approach | DOI: `10.1109/TAES.2025.3637795`
- `[S4]` `J2026_042` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): D. Jin, J. Qiu, W. Ji, and T. Wang — Integrated Attitude-Orbit Control for Spacecraft With Prescribed Performance via Fully Actuated System Approach | DOI: `10.1109/TAES.2025.3637795`
- `[S4]` `J2026_061` (2026, *IEEE Transactions on Automation Science and Engineering*): Z. Lin, D. Jin, X. Liu, S. Feng, and T. Wang — Prescribed Performance Control of Spacecraft: A Fully Actuated System Approach With Experimental Validation | DOI: `10.1109/TASE.2026.3735916`
- `[S4]` `J2026_062` (2026, *Aerospace Science and Technology*): Z. Lin and B. Wu — Safety-critical control for multiple spacecraft close-proximity inspection | DOI: `10.1016/j.ast.2025.110938`
- `[S4]` `J2026_072` (2026, *Science China Information Sciences*): K. Liu, Z. Yao, M. Liu, and G. Duan — Constrained Spacecraft Attitude Prescribed Performance Control based on Fixed-time Disturbance Observer and Fully Actuated System Approach | DOI: `10.1360/s11432-025-5097-7`
- `[S4]` `J2026_085` (2026, *IEEE/ASME Transactions on Mechatronics*): X. Zou, H.-J. Sun, D. Meng, T. Guo, and B. Liang — Practical Prescribed-Time Trajectory Tracking Control for a Novel Tendon-Driven Space Manipulator via Fully Actuated System Approaches | DOI: `10.1109/TMECH.2025.3528990`
- `[S4]` `J2026_145` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): K. Zhang, L. Luo, G. Xie, Z. Ning, G. Su, and J. Sun — Constrained Trajectory Planning and Control for Space Manipulator Capture Tasks Using an Improved Bi-level MOPSO Algorithm | DOI: `10.1109/TAES.2026.3727221`
- `[S4]` `J2026_168` (2026, *IEEE Transactions on Automation Science and Engineering*): Q. Zheng and K. Sun — Resilient Secure Tracking Control for Attitude-Orbit Integrated Spacecraft With Aperiodic DoS Attacks: A Fully Actuated System Approach | DOI: `10.1109/TASE.2026.3709748`
- `[S4]` `J2025_035` (2025, *IEEE Transactions on Aerospace and Electronic Systems*): Y. H. Yang, K. Zhang, Z. H. Chen, X. F. Yang, and G. R. Duan — Distributionally Robust Model Predictive Control for Trajectory Tracking of Space Manipulator Based on Fully Actuated System Approach | DOI: `10.1109/TAES.2025.3558184`
- `[S4]` `J2025_061` (2025, *IEEE Transactions on Automation Science and Engineering*): S. Jia, J. Qiu, and T. Wang — High-order Fully Actuated System Approach based Attitude Stabilization for Underactuated Rigid and Flexible Spacecraft | DOI: `10.1109/TASE.2025.3567541`
- `[S4]` `J2025_069` (2025, *IEEE Transactions on Aerospace and Electronic Systems*): Z. Feng, M. Liu, L. Zhang, X. Cao, and G. Duan — Leader-follower attitude coordination control for spacecraft formations with Gaussian processes | DOI: `10.1109/TAES.2025.3568420`
- `[S4]` `J2025_102` (2025, *Aerospace Science and Technology*): W. Dian, W. Yunhua, X. Hongyi, B.-Z. Franco, and X. Chen — Scheduled input shaping based attitude agile control for flexible spacecraft with vibration suppression | DOI: `10.1016/j.ast.2025.110355`
- `[S4]` `J2025_111` (2025, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): D. Jin, Y. Bi, T. Wang, J. Qiu, and H. Gao — Twistors-Based Attitude-Orbit Integrated Control for Spacecraft: A High-Order Fully Actuated System Approach | DOI: `10.1109/TSMC.2024.3519436`
- `[S4]` `J2024_030` (2024, *IEEE Transactions on Aerospace and Electronic Systems*): K.-X. Cui, G.-R. Duan, D.-W. Zhang, and D.-K. Gu — Discrete-Time High-Order Fully Actuated Adaptive Stabilization Control for a Type of Combined Spacecraft With Unknown Parameters | DOI: `10.1109/TAES.2024.3360948`
- `[S4]` `J2024_031` (2024, *IEEE Transactions on Automation Science and Engineering*): K.-X. Cui, G.-R. Duan, and M.-Z. Hou — Discrete-Time Model Reference Tracking Control for A Class of Combined Spacecraft: A High-Order Fully Actuated System Approach | DOI: `10.1109/TASE.2023.3335106`
- `[S4]` `J2024_040` (2024, *IEEE Transactions on Aerospace and Electronic Systems*): Q.-Z. Liu, L. Zhang, B. Sun, Y. Xiao, and G.-W. Fan — Fixed-Time Disturbance Observer-Based Attitude Prescribed Performance Predictive Control for Flexible Spacecraft | DOI: `10.1109/TAES.2024.3359591`
- `[S4]` `J2023_014` (2023, *IEEE/ASME Transactions on Mechatronics*): D.-W. Zhang, G.-P. Liu, and L. Cao — Constrained Cooperative Control for High-Order Fully Actuated Multiagent Systems With Application to Air-Bearing Spacecraft Simulators | DOI: `10.1109/TMECH.2022.3223927`
- `[S4]` `J2023_016` (2023, *IEEE/CAA Journal of Automatica Sinica*): F. Zhang and G. Duan — Coupled Dynamics and Integrated Control for Position and Attitude Motions of Spacecraft: A Survey | DOI: `10.1109/JAS.2023.123306`
- `[S4]` `J2022_018` (2022, *Science China Information Sciences*): T. Zhao and G.-R. Duan — Fully actuated system approach to attitude control of flexible spacecraft with nonlinear time-varying inertia | DOI: `10.1007/s11432-021-3349-3`
- `[S3]` `J2026_023` (2026, *International Journal of Systems Science*): X. Gao, M. Chen, and K. L. Teo — Fully-actuated system method for prescribed-time elliptical orbital spacecraft rendezvous | DOI: `10.1080/00207721.2026.2640482`
- `[S3]` `J2026_051` (2026, *International Journal of Systems Science*): Y. Li, F. Zhang, and Z. Gao — Attitude control for dumbbell-shaped spacecraft subject to parameter uncertainty via fully-actuated system approach and deep reinforcement learning | DOI: `10.1080/00207721.2026.2645178`
- `[S3]` `J2026_063` (2026, *International Journal of Fuzzy Systems*): K. Liu, J. Li, and M. Liu — Fuzzy Neuro-adaptive Observer-Based Fault-Tolerant Control for Flexible Spacecraft Attitude Maneuver with Pointing Constraints | DOI: `10.1007/s40815-025-02028-7`
- `[S3]` `J2026_115` (2026, *Acta Aeronautica et Astronautica Sinica (航空学报)*): B. Wang, Y. Lian, and P. Wang — Prescribed performance sliding mode control for high-speed morphing vehicles based on high-order fully-actuated systems
- `[S3]` `J2026_116` (2026, *Journal of the Franklin Institute*): Q. Wang and F. He — Sliding mode control for spacecraft attitude tracking based on fully actuated system approach | DOI: `10.1016/j.jfranklin.2025.108124`
- `[S3]` `J2026_119` (2026, *Applied Mathematics and Computation*): X. Wu and W. Sun — Adaptive fault tolerant optimal control for high-order fully actuated system and its application in spacecraft attitude tracking using reinforcement learning | DOI: `10.1016/j.amc.2025.129774`
- `[S3]` `J2026_124` (2026, *International Journal of Systems Science*): F.-Z. Xiao, Y.-H. Yu, and L.-Q. Chen — A symmetric fully actuated system framework for unwinding-free spacecraft attitude control | DOI: `10.1080/00207721.2026.2640478`
- `[S3]` `J2026_125` (2026, *Nonlinear Dynamics*): F.-Z. Xiao and L.-Q. Chen — Attitude control of in-orbit liquid-filled spacecraft within a fully actuated system framework | DOI: `10.1007/s11071-025-12101-3`
- `[S3]` `J2025_032` (2025, *Asian Journal of Control*): K.-X. Cui, G.-R. Duan, and Y. Cui — Discrete-time high-order fully actuated robust stabilization control for a type of combined spacecraft subject to uncertainties | DOI: `10.1002/asjc.3574`
- `[S3]` `J2025_046` (2025, *Nonlinear Dynamics*): Z. Zhang, J. Chen, C. Chen, G. Zheng, Z. Song, and Y. Chen — Fixed-time fault-tolerant attitude consensus control for multiple spacecraft via fully actuated system approaches | DOI: `10.1007/s11071-025-11598-y`
- `[S3]` `J2025_053` (2025, *Journal of the Franklin Institute*): D. Wang, Y. Wu, C. Yue, and S. Ma — Fully actuated system-based active disturbance rejection saturated attitude control for flexible spacecraft | DOI: `10.1016/j.jfranklin.2025.107613`
- `[S3]` `J2025_075` (2025, *Control Engineering Practice*): Q.-Z. Liu, L. Zhang, Y. Xiao, L. Zhang, and G.-W. Fan — Predictive sliding mode control for flexible spacecraft attitude tracking with multiple disturbances | DOI: `10.1016/j.conengprac.2024.106160`
- `[S3]` `J2024_005` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): D. Zhang and G. Liu — A high-order fully actuated predictive control approach of spacecraft flying-around under time-variant communication constraints | DOI: `10.7527/S1000-6893.2023.28633`
- `[S3]` `J2024_006` (2024, *International Journal of Systems Science*): D.-W. Zhang and G.-P. Liu — A high-order fully actuated predictive control approach for spacecraft flying-around | DOI: `10.1080/00207721.2024.2315223`
- `[S3]` `J2024_015` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): G. Duan and G. Liu — Adaptive prescribed control of position and attitude of combined spacecraft based on fully actuated system approach
- `[S3]` `J2024_017` (2024, *International Journal of Systems Science*): Y. Xing, Z. Yin, and C. Wei — Appointed-time safety-guaranteed control for spacecraft flying around non-cooperative target based on fully actuated system theory | DOI: `10.1080/00207721.2024.2313648`
- `[S3]` `J2024_018` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): M. Lu, X. Chen, F. Wu, and X. Cao — Attitude maneuver control of spacecraft based on second-order fully actuated system under attitude constraints
- `[S3]` `J2024_019` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): C. Duan, S. Xiaodong, H. Qinglei, and W. Huaining — Attitude tracking of underactuated spacecraft based on transverse function
- `[S3]` `J2024_048` (2024, *International Journal of Systems Science*): Q. Wang and Y. Jin — Fully actuated system approach for spacecraft rendezvous system with actuator saturation | DOI: `10.1080/00207721.2024.2317349`
- `[S3]` `J2024_052` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): Z. Yin, Y. Xing, F. Han, C. Wei, and Y. Liao — Fully-actuated prescribed performance control of spacecraft formation for flying cooperatively around non-cooperative target
- `[S3]` `J2024_064` (2024, *IET Control Theory and Applications*): S. Li, K. Liu, M. Liu, and X. Cao — Neuro-adaptive prescribed performance control for spacecraft rendezvous based on the fully-actuated system approach | DOI: `10.1049/cth2.12736`
- `[S3]` `J2024_090` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): M. Liu, R. Fan, S. Qiu, and X. Cao — Spacecraft attitude-orbit prescribed performance control based on fully actuated system approach
- `[S3]` `J2024_106` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): 崔凯鑫 and 段广仁 — 基于干扰观测器的一类组合航天器高阶全驱抗干扰控制
- `[S3]` `J2024_108` (2024, *Acta Automatica Sinica (自动化学报)*): 王典, 吴云华, 岳程斐, and 马松靖 — 输入受限的挠性航天器全驱姿态饱和控制 | DOI: `10.16383/j.aas.c230691`
- `[S3]` `J2023_022` (2023, *Acta Astronautica*): F.-Z. Xiao and L.-Q. Chen — Fully actuated systems in terms of quaternions for spacecraft attitude control | DOI: `10.1016/j.actaastro.2023.04.031`
- `[S3]` `J2023_031` (2023, *Journal of the Franklin Institute*): D.-W. Zhang, G.-P. Liu, and L. Cao — Predictive control of discrete-time high-order fully actuated systems with application to air-bearing spacecraft simulator | DOI: `10.1016/j.jfranklin.2023.04.003`
- `[S3]` `J2022_009` (2022, *Journal of Systems Science and Complexity*): F. Xiao and L. Chen — Attitude Control of Spherical Liquid-Filled Spacecraft Based on High-Order Fully Actuated System Approaches | DOI: `10.1007/s11424-022-2055-y`
- `[S3]` `J2022_010` (2022, *Journal of Systems Science and Complexity*): G. Duan and G.-P. Liu — Attitude and Orbit Optimal Control of Combined Spacecraft via a Fully-Actuated System Approach | DOI: `10.1007/s11424-022-1492-y`
- `[S3]` `J2022_016` (2022, *Journal of Systems Science and Complexity*): Q. Zhao and G.-R. Duan — Fully Actuated System Approach for 6DOF Spacecraft Control Based on Extended State Observer | DOI: `10.1007/s11424-022-1498-5`
- `[S3]` `J2022_020` (2022, *Journal of Systems Science and Complexity*): G. Liu, K. Zhang, and B. Li — Fully-actuated system approach based optimal attitude tracking control of rigid spacecraft with actuator saturation | DOI: `10.1007/s11424-022-1515-8`

### 2. 无人机与空中平台（四旋翼 / 直升机 / 倾转旋翼 / 空中机械臂）（共 35 篇）

- `[S4]` `J2026_003` (2026, *Aerospace Science and Technology*): Aqeel-Ur-Rehman and C. Cai — A unified high-order fully actuated system approach with active disturbance rejection control for robust quadrotor trajectory tracking | DOI: `10.1016/j.ast.2026.113297`
- `[S4]` `J2026_027` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): C. Gu, Q. Wu, Y.-W. Wang, and W.-A. Zhang — Prescribed Performance Disturbance Rejection Tracking Control of UAVs Via High-Order Fully Actuated System Approach | DOI: `10.1109/TAES.2025.3623614`
- `[S4]` `J2026_057` (2026, *Aerospace Science and Technology*): W. Li, J. Li, J. Wu, B. Li, V. Sreeram, and Y. Wei — Robust trajectory tracking control for unmanned aerial manipulators based on unscented Kalman filter and high-order fully-actuated approach | DOI: `10.1016/j.ast.2026.113577`
- `[S4]` `J2026_087` (2026, *Aerospace Science and Technology*): L. Qiu, Y. Ma, Y. Liu, J. Qiu, and F. Deng — Online-optimized high-order fully actuated generalized predictive control for quadrotor UAV attitude tracking | DOI: `10.1016/j.ast.2026.113151`
- `[S4]` `J2026_092` (2026, *IEEE Transactions on Cybernetics*): Y. Shi, R. Wang, H. Li, L. Wu, and Y. Zeng — High-Order Fully Actuated System Approach-Based Controller Design for Tailsitter in Flight Mode Transitions | DOI: `10.1109/TCYB.2025.3639150`
- `[S4]` `J2026_108` (2026, *IEEE Transactions on Control Systems Technology*): Y. Wang, L. Zhang, Y. Liu, X. Yang, and Y. Zhu — Flexbee: A Grasping and Perching UAV Based on Soft Vector-Propulsion Nozzle | DOI: `10.1109/TCST.2026.3692720`
- `[S4]` `J2026_121` (2026, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): Y. Wu, M. Chen, S. Shao, Z. Zhu, and M. Chadli — Distributed Event-Triggered Critic Control for UAV Swarms With Privacy-Preserving Mechanisms: A Fully-Actuated System Approach | DOI: `10.1109/TSMC.2026.3712467`
- `[S4]` `J2026_127` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): L. Xu, X. Wang, and G. Duan — Hierarchical Predictive Sliding Mode Control for Underactuated UAV: An FAS Approach | DOI: `10.1109/TAES.2026.3721474`
- `[S4]` `J2026_156` (2026, *IEEE Transactions on Cybernetics*): K. Zhang, Q. Miao, and B. Jiang — Learning-Based Fault-Tolerant Optimal Formation Control of Helicopters: An Incremental Fully Actuated System Approach | DOI: `10.1109/TCYB.2025.3610020`
- `[S4]` `J2026_173` (2026, *IEEE/ASME Transactions on Mechatronics*): Y. Zhu, D. Jin, L. Zhang, L. Zhang, X. Yang, and G. Duan — FAQts: A Class of Fully Actuated Quadrotor Based on Twin Servos | DOI: `10.1109/TMECH.2025.3639086`
- `[S4]` `J2026_174` (2026, *IEEE/ASME Transactions on Mechatronics*): Y. Zhu, J. Liu, L. Zhang, M. Cao, X. Liu, and G. Duan — FAH-ptf: A Class of Fully Actuated Hexacopter Based on Passively-Tilting Frame | DOI: `10.1109/TMECH.2026.3660910`
- `[S4]` `J2025_041` (2025, *IEEE Transactions on Aerospace and Electronic Systems*): Y. Xu, B. Jiang, M. M. Polycarpou, and B. Li — Fault-Tolerant Game Control for Quadrotor Helicopters' Formation: A Fully Actuated System Approach | DOI: `10.1109/TAES.2024.3513272`
- `[S4]` `J2025_043` (2025, *IEEE/ASME Transactions on Mechatronics*): Z. Li, Y. Yang, X. Yu, C. Liu, O. Kaynak, and H. Gao — Fixed-Time Control of a Novel Thrust-Vectoring Aerial Manipulator via High-Order Fully Actuated System Approach | DOI: `10.1109/TMECH.2024.3400015`
- `[S4]` `J2025_055` (2025, *Aerospace Science and Technology*): J. Hu, Y. Xu, and B. Jiang — Game-based fault-tolerant formation containment control for fixed-wing UAVs under the fully actuated system framework | DOI: `10.1016/j.ast.2025.110052`
- `[S4]` `J2025_068` (2025, *IEEE Transactions on Aerospace and Electronic Systems*): X. Kong, Y. Xia, Z. Sun, S. Zhang, and W. Ning — Trajectory Tracking and Real-Time Obstacle Avoidance for Differentially Flat UAV Under Disturbances and Measurement Noises | DOI: `10.1109/TAES.2025.3613474`
- `[S4]` `J2025_077` (2025, *IEEE Transactions on Intelligent Vehicles*): Y. Wang, Z. Wang, G. Wang, and L. Chen — Modeling and Control of A Coaxial Pendulum Drone | DOI: `10.1109/TIV.2024.3454340`
- `[S4]` `J2024_027` (2024, *IEEE Transactions on Robotics*): L. Chen, J. Xiao, Y. Zheng, N. A. Alagappan, and M. Feroskhan — Design, Modeling, and Control of a Coaxial Drone | DOI: `10.1109/TRO.2024.3354161`
- `[S4]` `J2024_065` (2024, *IEEE Transactions on Cybernetics*): Y. Ma, K. Zhang, and B. Jiang — Neuroadaptive Cooperative Fault-Tolerant Control of Heterogeneous Multiagent Systems Based on Fully Actuated System Approaches | DOI: `10.1109/TCYB.2023.3318254`
- `[S3]` `J2026_043` (2026, *Control Engineering Practice*): D. Jin, R. Qiu, J. Qiu, and T. Wang — Prescribed performance control for a novel quadrotor based on the fully actuated system approach and an extended state observer | DOI: `10.1016/j.conengprac.2025.106671`
- `[S3]` `J2026_045` (2026, *International Journal of Control, Automation, and Systems*): C. Ju, G. Zhao, and S. Huang — Local Refined Relaxed TP Model Transformation-Based Fuzzy Controller Design for Quadrotors | DOI: `10.1007/s12555-026-00185-5`
- `[S3]` `J2026_065` (2026, *Robotics and Autonomous Systems*): Z. Liu, X. Zhang, and P. Li — Fast-convergent GA-APO for real-time UAV path planning with fully actuated robust tracking | DOI: `10.1016/j.robot.2026.105476`
- `[S3]` `J2026_073` (2026, *Control Engineering Practice*): S. Lu, K. Tsakalis, and Y. Chen — A novel transformable UAV: HOFA modeling, control, and experimental validations | DOI: `10.1016/j.conengprac.2026.106990`
- `[S3]` `J2026_074` (2026, *Acta Aeronautica et Astronautica Sinica (航空学报)*): Y. Lu, K. Zhang, and B. Jiang — Hierarchical fault-tolerant formation control for unmanned helicopters based on fully-actuated system approach
- `[S3]` `J2026_079` (2026, *IEEE Transactions on Vehicular Technology*): B. Meng, K. Zhang, B. Jiang, and L. Guo — Fully Actuated System Approach-Based Prescribed Time Fault-Tolerant Control and Hierarchical Structure Avoidance Collision for Multiple Unmanned Helicopters | DOI: `10.1109/TVT.2026.3663621`
- `[S3]` `J2026_081` (2026, *Control Engineering Practice*): B. Meng, K. Zhang, and B. Jiang — Hierarchical structure-based adaptive fault-tolerant control and collision avoidance for multiple fixed-wing UAVs: A fully actuated system approach | DOI: `10.1016/j.conengprac.2026.106763`
- `[S3]` `J2026_095` (2026, *ISA Transactions*): H. Sun, X. Gu, K. Zheng, and Z. Wei — Finite-time swing attenuation for differentially flat quadrotor slung-load systems via robust AFITSM-OSMC partitioned control | DOI: `10.1016/j.isatra.2026.06.034`
- `[S3]` `J2026_111` (2026, *Acta Aeronautica et Astronautica Sinica (航空学报)*): X. Wang, G. Tian, B. Li, and Z. He — Fully actuated anti-disturbance control for quadrotor UAVs based on dynamic compensator
- `[S3]` `J2025_051` (2025, *Nonlinear Dynamics*): B. Meng, L. Shen, K. Zhang, and J. Xia — Fully actuated system approach-based fault-tolerant formation reconstruction control and optimal task assignment for fixed-wing UAVs | DOI: `10.1007/s11071-024-10246-1`
- `[S3]` `J2025_062` (2025, *International Journal of Systems Science*): S. Lu, T. Konstantinos, and Y. Chen — High-order fully actuated system approach for quadrotor control based on extended state observers | DOI: `10.1080/00207721.2025.2512208`
- `[S3]` `J2025_079` (2025, *International Journal of Systems Science*): G. Liu, J. Xia, Q. Miao, B. Jiang, and K. Zhang — Neural-based fault-tolerant control using fully actuated system approach and intelligent safe planning for helicopter formation | DOI: `10.1080/00207721.2025.2511205`
- `[S3]` `J2024_022` (2024, *ISA Transactions*): X. Wang and G. Duan — Comprehensive reconstructions and predictive control for quadrotor UAV information gathering tracking missions based on fully actuated system approaches | DOI: `10.1016/j.isatra.2024.01.020`
- `[S3]` `J2024_082` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): Q. Zhang, Y. Liu, H. Sun, and B. Zhu — Robust cooperative tracking control for close formation of fixed-wing unmanned aerial vehicles
- `[S3]` `J2024_105` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): 杨梓霄, 李世尧, 魏晨, 李湛, and 朱波 — 基于低阶干扰估计器的欠驱动三自由度直升机鲁棒控制
- `[S3]` `J2025_001` (2024, *International Journal of Robust and Nonlinear Control*): Y. Chen, D. Zhang, Z. Zhang, and H. Zhang — A High‐Order Fully Actuated System Approach for Prescribed Performance Tracking Control of Quadrotor Unmanned Aerial Vehicle With Time‐Varying Uncertain Aerodynamic Parameters and Disturbances | DOI: `10.1002/rnc.7793`
- `[S3]` `J2023_018` (2023, *IEEE Control Systems Letters*): S. Lu, K. Tsakalis, and Y. Chen — Development and Application of a Novel High-Order Fully Actuated System Approach-Part I: 3-DOF Quadrotor Control | DOI: `10.1109/LCSYS.2022.3232305`

### 3. 机械臂与精密运动平台（刚/柔性关节 / 绳驱 / 水下 / 龙门平台）（共 18 篇）

- `[S5]` `J2026_035` (2026, *Automatica*): S. Jia, Z. Liu, J. Qiu, and H. Gao — Feed velocity based coordinated contouring control for dual-linear-motor-driven gantry stage via fully actuated system approach | DOI: `10.1016/j.automatica.2026.113049`
- `[S4]` `J2026_085` (2026, *IEEE/ASME Transactions on Mechatronics*): X. Zou, H.-J. Sun, D. Meng, T. Guo, and B. Liang — Practical Prescribed-Time Trajectory Tracking Control for a Novel Tendon-Driven Space Manipulator via Fully Actuated System Approaches | DOI: `10.1109/TMECH.2025.3528990`
- `[S4]` `J2026_145` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): K. Zhang, L. Luo, G. Xie, Z. Ning, G. Su, and J. Sun — Constrained Trajectory Planning and Control for Space Manipulator Capture Tasks Using an Improved Bi-level MOPSO Algorithm | DOI: `10.1109/TAES.2026.3727221`
- `[S4]` `J2026_147` (2026, *IEEE Transactions on Cybernetics*): C.-H. Zhang, L.-H. Zhang, L. Wang, Y. Zhang, W. Ding, and C.-C. Hua — Dynamic Event-Triggered Control for Flexible Joint Robot Based on Fully Actuated System Approach | DOI: `10.1109/TCYB.2025.3630202`
- `[S4]` `J2025_035` (2025, *IEEE Transactions on Aerospace and Electronic Systems*): Y. H. Yang, K. Zhang, Z. H. Chen, X. F. Yang, and G. R. Duan — Distributionally Robust Model Predictive Control for Trajectory Tracking of Space Manipulator Based on Fully Actuated System Approach | DOI: `10.1109/TAES.2025.3558184`
- `[S4]` `J2025_043` (2025, *IEEE/ASME Transactions on Mechatronics*): Z. Li, Y. Yang, X. Yu, C. Liu, O. Kaynak, and H. Gao — Fixed-Time Control of a Novel Thrust-Vectoring Aerial Manipulator via High-Order Fully Actuated System Approach | DOI: `10.1109/TMECH.2024.3400015`
- `[S4]` `J2025_067` (2025, *Mechanical Systems and Signal Processing*): N. Jiang, Z. Zhang, and Y. Wu — DO-based tracking controller of n-link flexible-joint manipulators with output constraints: An FAS approach | DOI: `10.1016/j.ymssp.2025.113341`
- `[S4]` `J2025_087` (2025, *IEEE Transactions on Industrial Electronics*): H. Jiang, Y. Yang, C. Hua, X. Li, and F. Lu — Predefined-Time Composite Fuzzy Adaptive Control for Flexible-Joint Manipulator System With High-Order Fully Actuated Control Approach | DOI: `10.1109/TIE.2024.3515255`
- `[S3]` `J2026_014` (2026, *International Journal of Systems Science*): H. Dai, H. Wang, Y. Tian, and L. Zhang — Fully actuated system theory and extended state observer based model free prescribed-time control for series elastic actuator manipulator | DOI: `10.1080/00207721.2026.2643695`
- `[S3]` `J2026_039` (2026, *Journal of Systems Science and Complexity*): H. Jiang, Y. Yang, X. Sheng, and J. Li — Barrier Function-Based Adaptive Controller Design for Flexible-Joint Robots: Fully-Actuated System Approach | DOI: `10.1007/s11424-026-5062-6`
- `[S3]` `J2026_059` (2026, *Control Engineering Practice*): W. Lin, W. Liu, X. Zou et al — A novel model predictive control law for over-actuated space cable-driven manipulators | DOI: `10.1016/j.conengprac.2026.106819`
- `[S3]` `J2026_178` (2026, *Acta Astronautica*): X. Zou, R. Chen, Y. Liu, D. Meng, and H.-J. Sun — Tunable predefined-time trajectory tracking control for cable-driven space manipulators using extended state observer via fully-actuated system approaches | DOI: `10.1016/j.actaastro.2026.02.003`
- `[S3]` `J2025_115` (2025, *ISA Transactions*): Q. Wang, W. Xu, and Z. Leng — Adaptive event-triggered anti-windup trajectory tracking control for robotic manipulator | DOI: `10.1016/j.isatra.2025.10.020`
- `[S3]` `J2024_045` (2024, *IEEE Transactions on Circuits and Systems II: Express Briefs*): C. Yan, J. Xia, J. H. Park, J.-e. Feng, and X. Xie — Fully Actuated System Approach-Based Dynamic Event-Triggered Control With Guaranteed Transient Performance of Flexible-Joint Robot: Experiment | DOI: `10.1109/TCSII.2024.3367180`
- `[S3]` `J2024_097` (2024, *Acta Automatica Sinica (自动化学报)*): G. Cai, Y. Xiao, C. Hu, X. Yang, and Y. Fan — Time-varying Output Constraint Control of High-order Strict-feedback Systems Based on Fully Actuated System Approach | DOI: `10.16383/j.aas.c230441`
- `[S3]` `J2023_037` (2023, *International Journal of Robust and Nonlinear Control*): G. Tian and G. Duan — Robust model reference tracking for uncertain second-order nonlinear systems with application to robot manipulator | DOI: `10.1002/rnc.6450`
- `[S3]` `J2023_038` (2023, *Control Theory and Technology*): E. Kang, Y. Liu, and H. Qiao — Sliding mode-based adaptive tube model predictive control for robotic manipulators with model uncertainty and state constraints | DOI: `10.1007/s11768-023-00174-7`
- `[S3]` `J2022_031` (2022, *Journal of Systems Science and Complexity*): H. Sun, L. Huang, and L. He — Research on the Trajectory Tracking Control of a 6-DOF Manipulator Based on Fully-Actuated System Models | DOI: `10.1007/s11424-022-2045-0`

### 4. 欠驱动机械系统（吊车 / 倒立摆 / 惯性轮摆 / TORA / 球杆 / Acrobot / 弹簧质量）（共 13 篇）

- `[S5]` `J2026_144` (2026, *Automatica*): Z.-C. Zhang, Y. Gao, Y.-Q. Wu, and G.-R. Duan — Composite-variable-based adaptive tracking control for state-constrained nonlinear systems and its application to crane | DOI: `10.1016/j.automatica.2026.113248`
- `[S4]` `J2026_020` (2026, *Science China Information Sciences*): G. Duan, L. Hu, S. Zhang, Z. Chen, and L. Liu — Substabilization for coupled-inverted pendulums with input failure: a fully actuated system approach | DOI: `10.1007/s11432-025-4621-1`
- `[S4]` `J2026_033` (2026, *IEEE/CAA Journal of Automatica Sinica*): P. Li, G.-R. Duan, B. Zhang, and Y. Wang — Nonlinear Control of Reaction Wheel Pendulum based on Fully Actuated System Approach
- `[S4]` `J2026_150` (2026, *IEEE/ASME Transactions on Mechatronics*): Z. Zhang, Y. Gao, and Y. Wu — FAS-Approach-Based Antiswing Control of Underactuated Overhead Double-Pendulum Cranes Under Uncertain Friction: An Adaptive Method | DOI: `10.1109/TMECH.2026.3694205`
- `[S4]` `J2026_151` (2026, *IEEE Transactions on Industrial Electronics*): M. Zhang, X. Liu, J. Zhao, and G. Duan — Fully Actuated System Approach-Based Neuroadaptive Control for Underactuated 4-DOF Tower Crane Systems With Unavailable States and Input Dead Zones | DOI: `10.1109/TIE.2025.3603033`
- `[S4]` `J2026_152` (2026, *IEEE Transactions on Industrial Electronics*): M. Zhang, X. Liu, J. Zhao, and G. Duan — Fully Actuated System Approach-Based Neuroadaptive Control for Underactuated 4-DOF Tower Crane Systems With Unavailable States and Input Dead Zones | DOI: `10.1109/TIE.2025.3603033`
- `[S4]` `J2025_020` (2025, *IEEE Transactions on Industrial Electronics*): Y. Gao, Z. Zhang, N. Jiang, and Y. Wu — Anti-Swing Control for Double-Pendulum Overhead Cranes: From Underactuated to FAS Configuration | DOI: `10.1109/TIE.2025.3544192`
- `[S4]` `J2025_077` (2025, *IEEE Transactions on Intelligent Vehicles*): Y. Wang, Z. Wang, G. Wang, and L. Chen — Modeling and Control of A Coaxial Pendulum Drone | DOI: `10.1109/TIV.2024.3454340`
- `[S4]` `J2025_123` (2025, *Mechanical Systems and Signal Processing*): H. Zhang, W. Ding, C. Hua, and B. Lu — Predictive control of single pendulum cranes under actuated/underactuated state constraints: A higher-order fully actuated approach | DOI: `10.1016/j.ymssp.2025.113411`
- `[S4]` `J2024_003` (2024, *IEEE/ASME Transactions on Mechatronics*): F. Yao, G. Tian, A. Wu, G.-R. Duan, and H. Kong — A High-Order Fully Actuated System Approach to Control of Overhead Cranes | DOI: `10.1109/TMECH.2024.3446670`
- `[S4]` `J2024_009` (2024, *IEEE Transactions on Cybernetics*): F. Yao, A. Wu, M. Golestani, D. Liu, G. Duan, and H. Kong — Adaptive Tracking Control for Underactuated Double Pendulum Overhead Cranes With Variable Cable Length | DOI: `10.1109/TCYB.2024.3388548`
- `[S3]` `J2026_100` (2026, *International Journal of Systems Science*): Z. Wang, X. Xin, and Y. Liu — Controlling folded configurations of 2-link underactuated gymnastic robot: strong stabilization and minimal-order controllers | DOI: `10.1080/00207721.2025.2557002`
- `[S3]` `J2026_125` (2026, *Nonlinear Dynamics*): F.-Z. Xiao and L.-Q. Chen — Attitude control of in-orbit liquid-filled spacecraft within a fully actuated system framework | DOI: `10.1007/s11071-025-12101-3`

### 5. 水面/水下无人艇与船舶（USV / AUV / 船舶 / 气垫船）（共 5 篇）

- `[S4]` `J2025_027` (2025, *IEEE Transactions on Cybernetics*): Z.-C. Zhang, G.-R. Duan, and Y.-Q. Wu — Continuous Stabilization Controller for Nonlinear Systems With Two Piecewise Controllers and Its Application to Underactuated Ships | DOI: `10.1109/TCYB.2025.3535768`
- `[S3]` `J2026_026` (2026, *Asian Journal of Control*): Q. Pan, X. Peng, Y. Lv, and Y. Tian — Global exponential stabilization of underactuated surface vessel with high‐order fully actuated control approach | DOI: `10.1002/asjc.3782`
- `[S3]` `J2026_078` (2026, *Communications in Nonlinear Science and Numerical Simulation*): R. Meng, C. Hua, and K. Li — Dual-channel event-triggered control for uncertain unmanned surface vessels | DOI: `10.1016/j.cnsns.2026.110222`
- `[S3]` `J2026_123` (2026, *Neurocomputing*): Y.-Z. Xiang and Z. Xiang — Learning-based optimal formation for multi-unmanned surface vessels via fully actuated system approach | DOI: `10.1016/j.neucom.2025.132369`
- `[S3]` `J2024_010` (2024, *Journal of Systems Science and Complexity*): L. Zhang, P. Wang, C. Qian, and C. Hua — Adaptive Trajectory Tracking Error Constraint Control of Unmanned Underwater Vehicle Based on a Fully Actuated System Approach | DOI: `10.1007/s11424-024-3445-0`

### 6. 移动机器人、智能车辆与非完整/链式系统（Unicycle / Brockett / 广义链式 / 车队）（共 16 篇）

- `[S5]` `J2025_036` (2025, *Science China Information Sciences*): G. Duan — A FAS approach for stabilization of generalized chained systems: multi-vector case | DOI: `10.1007/s11432-024-4335-9`
- `[S5]` `J2024_001` (2024, *Science China Information Sciences*): G. R. Duan — A FAS approach for stabilization of generalized chained forms: part 2. Continuous control laws | DOI: `10.1007/s11432-023-3920-8`
- `[S5]` `J2024_002` (2024, *Science China Information Sciences*): G. R. Duan — A FAS approach for stabilization of generalized chained forms: part 1. Discontinuous control laws | DOI: `10.1007/s11432-022-3730-8`
- `[S5]` `J2024_043` (2024, *IEEE Transactions on Cybernetics*): G. R. Duan — Fully Actuated System Approach for Control: An Overview | DOI: `10.1109/TCYB.2024.3457584`
- `[S5]` `J2023_012` (2023, *Journal of Systems Science and Complexity*): G.-R. Duan — Brockett’s Second Example: A FAS Approach Treatment | DOI: `10.1007/s11424-023-2282-x`
- `[S5]` `J2022_011` (2022, *Journal of Systems Science and Complexity*): G.-R. Duan — Brockett’s First Example: An FAS Approach Treatment | DOI: `10.1007/s11424-022-2090-8`
- `[S4]` `J2026_048` (2026, *Information Sciences*): M. Lei, Z. Zhu, Y. Pan, and Y. Lei — ESP-based prescribed performance formation control for vehicle platoon systems with input saturation: A fully actuated system approach | DOI: `10.1016/j.ins.2026.123161`
- `[S4]` `J2026_162` (2026, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): J. Zhang, Y. Liu, B. Niu, W. Li, and B. Zhang — Prescribed-Time Containment Control for Multiple Mobile Robot Systems | DOI: `10.1109/TSMC.2025.3650119`
- `[S4]` `J2025_027` (2025, *IEEE Transactions on Cybernetics*): Z.-C. Zhang, G.-R. Duan, and Y.-Q. Wu — Continuous Stabilization Controller for Nonlinear Systems With Two Piecewise Controllers and Its Application to Underactuated Ships | DOI: `10.1109/TCYB.2025.3535768`
- `[S4]` `J2025_039` (2025, *IEEE Transactions on Automation Science and Engineering*): Y. Gao, Z. Zhang, P. Huang, and Y. Wu — FAS-Based Anti-Disturbance Stabilization Control of Nonholonomic Systems: Theory and Experiment | DOI: `10.1109/TASE.2024.3397316`
- `[S4]` `J2025_045` (2025, *IEEE Transactions on Circuits and Systems I: Regular Papers*): J. Qiang, L. Li, C. Hua, X. Ren, and C. Liu — Fixed-Time Generalized VGESO-Based Trajectory Tracking Control for WMRs on Uneven Road: A Fully Actuated System Approach | DOI: `10.1109/TCSI.2025.3560091`
- `[S4]` `J2024_093` (2024, *IEEE/CAA Journal of Automatica Sinica*): Z. Zhang and G. Duan — Stabilization Controller of an Extended Chained Nonholonomic System With Disturbance: An FAS Approach | DOI: `10.1109/JAS.2023.124098`
- `[S3]` `J2026_006` (2026, *International Journal of Systems Science*): S. Cao and G. Duan — Bearing-only circumnavigation by a unicycle agent based on a fully actuated system approach | DOI: `10.1080/00207721.2026.2682436`
- `[S3]` `J2026_093` (2026, *Robotics and Autonomous Systems*): B. Song, Z. Shang, and Z. Wang — Trajectory tracking control of omni-directional mobile robots: A HOFA-LESO based approach | DOI: `10.1016/j.robot.2026.105492`
- `[S3]` `J2026_163` (2026, *International Journal of Systems Science*): J. Zhang, Y. Liu, Z. Zheng, and B. Niu — Prescribed-time control for nonholonomic systems: a fully actuated systems method | DOI: `10.1080/00207721.2026.2623144`
- `[S3]` `J2026_180` (2026, *Acta Automatica Sinica (自动化学报)*): 王东亨, 李兵强, 周素莹, 武涵, and 曹明明 — 基于全驱系统理论的永磁同步电机连续时变抗扰控制 | DOI: `10.16383/j.aas.c250527`

### 7. 电机、电力电子、微电网与磁悬浮伺服（PMSM / LSRM / 微电网 / 磁悬浮 / 柔性伺服）（共 13 篇）

- `[S4]` `J2026_049` (2026, *IEEE/ASME Transactions on Mechatronics*): P. Li, G.-R. Duan, B. Zhang, L. Wang, and Y. Wang — Output Position Control of Two-Mass Systems Based on Fully Actuated System and Singular Perturbation Approaches | DOI: `10.1109/TMECH.2025.3602374`
- `[S4]` `J2026_110` (2026, *IEEE Transactions on Power Delivery*): W. Wang, C. Chen, J. Yu, Y. Cao, Y. Li, and C. Deng — Fully Actuated Control of Point-to-Point VSC–HVDC Links for Frequency and DC Voltage Regulation in Asynchronous AC Systems | DOI: `10.1109/TPWRD.2026.3690660`
- `[S4]` `J2026_130` (2026, *IEEE Transactions on Transportation Electrification*): Y. Yang, Z. Li, C. Dai, and Z. Long — Nonlinear Robust Composite Levitation Control for Joint Structure of High-Speed Maglev Train Under External Disturbance and Time-Varying Model Parameters | DOI: `10.1109/TTE.2025.3641549`
- `[S4]` `J2026_131` (2026, *IEEE Transactions on Transportation Electrification*): Y. Yang, Z. Li, C. Dai, and Z. Long — Nonlinear Robust Composite Levitation Control for Joint Structure of High-Speed Maglev Train Under External Disturbance and Time-Varying Model Parameters | DOI: `10.1109/TTE.2025.3641549`
- `[S4]` `J2025_002` (2025, *IEEE Transactions on Power Electronics*): Y. Wei and B. Zhang — A Robust Controller Based on High-Order Fully Actuated Approach for DC–DC Buck Converter With Constant Power Loads in DC Microgrids | DOI: `10.1109/TPEL.2025.3544683`
- `[S4]` `J2025_059` (2025, *IEEE Transactions on Industrial Electronics*): P. Li, G. Duan, B. Zhang, P. Wang, and Y. Wang — High-Order Fully Actuated Approach for Output Tracking Control of Flexible Servo Systems Subject to Uncertainties and Disturbances | DOI: `10.1109/TIE.2025.3531480`
- `[S4]` `J2024_032` (2024, *IEEE Transactions on Industrial Electronics*): Y. Yu, G.-P. Liu, Y. Huang, and J. M. Guerrero — Distributed learning-based secondary control for islanded DC microgrids: A high-order fully actuated system approach | DOI: `10.1109/TIE.2023.3273276`
- `[S4]` `J2024_069` (2024, *IEEE/CAA Journal of Automatica Sinica*): Y. Yu, G.-P. Liu, Y. Huang, and P. Shi — Optimal Cooperative Secondary Control for Islanded DC Microgrids via a Fully Actuated Approach | DOI: `10.1109/JAS.2023.123942`
- `[S4]` `J2023_023` (2023, *IEEE/ASME Transactions on Mechatronics*): P. Li and G. Duan — High-Order Fully Actuated Control Approaches of Flexible Servo Systems Based on Singular Perturbation Theory | DOI: `10.1109/TMECH.2023.3267085`
- `[S3]` `J2026_068` (2026, *International Journal of Systems Science*): Y.-y. Liu, Y.-t. Ma, L. Qiu, and F.-q. Deng — Predictive observer-compensated high-order fully actuated tracking control for linear switched reluctance machine | DOI: `10.1080/00207721.2026.2640475`
- `[S3]` `J2026_167` (2026, *International Journal of Systems Science*): X. Zheng, Y. Zhao, Q. Li, and P. Mattavelli — Current control of grid-forming LCL-type inverter with a fully actuated control strategy | DOI: `10.1080/00207721.2026.2633326`
- `[S3]` `J2026_180` (2026, *Acta Automatica Sinica (自动化学报)*): 王东亨, 李兵强, 周素莹, 武涵, and 曹明明 — 基于全驱系统理论的永磁同步电机连续时变抗扰控制 | DOI: `10.16383/j.aas.c250527`
- `[S3]` `J2025_105` (2025, *IEEE Open Journal of the Industrial Electronics Society*): C. Limones, N. Vázquez, R. Femat et al — Single-phase grid-connected Inverter with Predictive Control Cost Function for Leakage Current Mitigation and FAS Model | DOI: `10.1109/OJIES.2025.3566582`

### 8. 工业过程、液压/气动执行器与车辆主动悬架（CSTR / 气动 / 液压 / 悬架）（共 12 篇）

- `[S4]` `J2026_009` (2026, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): Y. Cao, L. Li, C. Hua, and C. Liu — Practical Prescribed-Time Fully Actuated Control of 2-DOF Pneumatic Parallel Mechanism With Hysteresis Compensation | DOI: `10.1109/TSMC.2026.3731032`
- `[S4]` `J2026_010` (2026, *IEEE Transactions on Cybernetics*): Y. Cao, L. Li, C. Hua, and J. Qiang — Practical Prescribed-Time Fully Actuated Tracking Control for 2-DOF Pneumatic Parallel Mechanism With Input Saturation | DOI: `10.1109/TCYB.2026.3732042`
- `[S4]` `J2026_140` (2026, *IEEE/CAA Journal of Automatica Sinica*): J. Zhang, Z. Chen, and G. Guo — A Distributed Braking Scheme for Heavy-Haul Trains Using Coupler Force Compensation | DOI: `10.1109/JAS.2025.125870`
- `[S4]` `J2026_141` (2026, *IEEE Transactions on Cybernetics*): B. Zhang, C. Hua, J. Zhou, J. Chen, and Y. Zhang — Adaptive Task-Space Control for Hydraulic Excavators Based on the High-Order Fully Actuated System Approach | DOI: `10.1109/TCYB.2026.3702736`
- `[S4]` `J2026_149` (2026, *Mechanical Systems and Signal Processing*): Y. Zhang, T. Huang, J. Zhao, Z. Liu, and M. Zhang — Event-triggered control and dynamical compensator for active suspension systems with high-order fully actuated system approach | DOI: `10.1016/j.ymssp.2026.114244`
- `[S4]` `J2025_022` (2025, *IEEE Transactions on Industrial Electronics*): M. Zhang, Z. Zhou, N. Sun, H. Geng, J. Zhao, and Z. Yang — Bioinspired Reference Model and Fully Actuated System Approach-Based Neuroadaptive Control for Uncertain Active Suspension Systems With Input Dead Zones | DOI: `10.1109/TIE.2025.3536552`
- `[S3]` `J2026_112` (2026, *Applied Mathematical Modelling*): C. Wang, J. Ye, Q. Guo, J. Wang, X. Dai, and T. Li — High-order fully actuated event-triggered control with external load compensation for electro-hydraulic servo systems | DOI: `10.1016/j.apm.2025.116349`
- `[S3]` `J2026_115` (2026, *Acta Aeronautica et Astronautica Sinica (航空学报)*): B. Wang, Y. Lian, and P. Wang — Prescribed performance sliding mode control for high-speed morphing vehicles based on high-order fully-actuated systems
- `[S3]` `J2026_164` (2026, *Journal of Process Control*): X. Zhang and G. Duan — Pseudo predictor for tracking control of fully actuated nonlinear systems with a constant input delay and application to a two-stage chemical reactor | DOI: `10.1016/j.jprocont.2026.103733`
- `[S3]` `J2025_006` (2025, *International Journal of Systems Science*): G. Wang, D. Yang, L. Lv et al — Active disturbance rejection control of hydraulic turbine based on fully actuated system theory | DOI: `10.1080/00207721.2025.2506007`
- `[S3]` `J2025_050` (2025, *Nonlinear Dynamics*): M. Zhang, Z. Zhou, N. Sun, and J. Zhao — Fully actuated system approach to robust control for uncertain active suspension systems | DOI: `10.1007/s11071-024-10746-0`
- `[S3]` `J2024_082` (2024, *Acta Aeronautica et Astronautica Sinica (航空学报)*): Q. Zhang, Y. Liu, H. Sun, and B. Zhu — Robust cooperative tracking control for close formation of fixed-wing unmanned aerial vehicles

### 9. 切换系统、脉冲/混合控制、主动容错与经典非线性基准（Switched / Impulsive / FTC / Lorenz / Isidori）（共 56 篇）

- `[S5]` `J2024_071` (2024, *Automatica*): Y. Ma, K. Zhang, and B. Jiang — Practical prescribed-time active fault-tolerant control for mixed-order heterogeneous multiagent systems: A fully actuated system approach | DOI: `10.1016/j.automatica.2024.111721`
- `[S5]` `J2023_011` (2023, *Automatica*): M. Cai, X. He, and D. Zhou — An active fault tolerance framework for uncertain nonlinear high-order fully-actuated systems | DOI: `10.1016/j.automatica.2023.110969`
- `[S4]` `J2026_004` (2026, *IEEE Transactions on Cybernetics*): M. Cai, X. He, and D. Zhou — Fault-Tolerant Control Redesign for Noisy High-Order Fully Actuated Systems | DOI: `10.1109/TCYB.2025.3632342`
- `[S4]` `J2026_034` (2026, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): S. Jia, L. Yuan, J. Qiu, T. Wang, and M. Li — Anti-Unwinding Active Fault-Tolerant Attitude Tracking Control for Uncertain Spacecraft via Fully Actuated System Approach | DOI: `10.1109/TSMC.2026.3659255`
- `[S4]` `J2026_037` (2026, *IEEE Transactions on Industrial Electronics*): S. Jia, J. Qiu, J. J. Rodriguez-Andina, and K. Chen — Synergistic Adaptive Robust Fault-Tolerant Control for Linear Motors: A Fully Actuated System Reference Model Approach | DOI: `10.1109/TIE.2026.3672733`
- `[S4]` `J2026_038` (2026, *IEEE Transactions on Industrial Electronics*): S. Jia, J. Qiu, J. J. Rodriguez-Andina, and K. Chen — Synergistic Adaptive Robust Fault-Tolerant Control for Linear Motors: A Fully Actuated System Reference Model Approach | DOI: `10.1109/TIE.2026.3672733`
- `[S4]` `J2026_052` (2026, *IEEE Transactions on Automation Science and Engineering*): Z. Li, G. Zong, X. Liu, H. Wang, X. Zhao, and S. Ding — Distributed Adaptive Optimal Fault-Tolerant Formation Containment Control for High-Order Nonlinear Multi-Agent Systems via a Fully Actuated System Approach | DOI: `10.1109/TASE.2026.3729684`
- `[S4]` `J2026_076` (2026, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): Y. Ma, K. Zhang, and B. Jiang — Composite-Learning-Based Fault-Tolerant Containment Control for Heterogeneous Fully Actuated Multiagent Systems | DOI: `10.1109/TSMC.2026.3704612`
- `[S4]` `J2026_077` (2026, *IEEE Transactions on Cybernetics*): Y. Ma, K. Zhang, and B. Jiang — Cross-Dimensional Fault-Tolerant Control of Heterogeneous Fully Actuated Multiagent Systems Against Hybrid Faults | DOI: `10.1109/TCYB.2026.3681627`
- `[S4]` `J2026_080` (2026, *Aerospace Science and Technology*): B. Meng, K. Zhang, B. Jiang, and S. Simani — Hierarchical Game-Based Collision Avoidance and Fault-Tolerant Formation Control for Unmanned Helicopters with Multiple Faults: A Fully Actuated System Approach | DOI: `10.1016/j.ast.2026.113979`
- `[S4]` `J2026_088` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): W. Ren, G.-R. Duan, M. Fu, and H. Kong — A Zonotopic Disturbance Observer and Fully Actuated System Framework for Fault-Tolerant Control of Discrete-Time Uncertain Nonlinear Systems | DOI: `10.1109/TAES.2026.3660803`
- `[S4]` `J2026_089` (2026, *IEEE Transactions on Aerospace and Electronic Systems*): W. Ren, G.-R. Duan, M. Fu, and H. Kong — A Zonotopic Disturbance Observer and Fully Actuated System Framework for Fault-Tolerant Control of Discrete-Time Uncertain Nonlinear Systems | DOI: `10.1109/TAES.2026.3660803`
- `[S4]` `J2026_090` (2026, *IEEE Transactions on Industrial Electronics*): W. Ren, H. Kong, J. H. Park, and G.-R. Duan — Fault-Tolerant Control for Nonlinear Systems Based on FAS Framework and Interval Estimation | DOI: `10.1109/TIE.2026.3722974`
- `[S4]` `J2026_156` (2026, *IEEE Transactions on Cybernetics*): K. Zhang, Q. Miao, and B. Jiang — Learning-Based Fault-Tolerant Optimal Formation Control of Helicopters: An Incremental Fully Actuated System Approach | DOI: `10.1109/TCYB.2025.3610020`
- `[S4]` `J2025_005` (2025, *IEEE Transactions on Industrial Informatics*): X. Liu, D. Zhou, and L. Sheng — Active Fault-Tolerant Control for Stochastic Fully Actuated Systems With Local Faults | DOI: `10.1109/TII.2025.3547025`
- `[S4]` `J2025_007` (2025, *IEEE Transactions on Cybernetics*): X. Liu, M. Chen, D. Zhou, and L. Sheng — Adaptive Actuator Fault-Tolerant Tracking Control for Stochastic High-Order Fully Actuated Systems | DOI: `10.1109/TCYB.2025.3535774`
- `[S4]` `J2025_041` (2025, *IEEE Transactions on Aerospace and Electronic Systems*): Y. Xu, B. Jiang, M. M. Polycarpou, and B. Li — Fault-Tolerant Game Control for Quadrotor Helicopters' Formation: A Fully Actuated System Approach | DOI: `10.1109/TAES.2024.3513272`
- `[S4]` `J2025_055` (2025, *Aerospace Science and Technology*): J. Hu, Y. Xu, and B. Jiang — Game-based fault-tolerant formation containment control for fixed-wing UAVs under the fully actuated system framework | DOI: `10.1016/j.ast.2025.110052`
- `[S4]` `J2025_073` (2025, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): X. Liu, D. Zhou, and L. Sheng — Adaptive Fault-Tolerance Control for Stochastic Fully Actuated Systems With Component Faults | DOI: `10.1109/TSMC.2025.3574164`
- `[S4]` `J2025_078` (2025, *IEEE Transactions on Cybernetics*): M. Gong, D. Zhou, L. Sheng, and X. He — Multicontroller-Based Fault-Tolerant Control for Uncertain High-Order Sub-Fully Actuated Systems | DOI: `10.1109/TCYB.2025.3560406`
- `[S4]` `J2025_093` (2025, *IEEE Transactions on Automation Science and Engineering*): Y. Ma, K. Zhang, and B. Jiang — Prescribed-Time Fault-Tolerant Containment Control of Fully Actuated Heterogeneous Multiagent Systems Without Estimations of Fault Parameters | DOI: `10.1109/TASE.2025.3555239`
- `[S4]` `J2025_104` (2025, *IEEE/ASME Transactions on Mechatronics*): W. Ren, G.-R. Duan, P. Li, and H. Kong — Set-Based Fault-Tolerant Control for Continuous-Time Nonlinear Systems: A Fully Actuated System Approach | DOI: `10.1109/TMECH.2025.3565876`
- `[S4]` `J2025_106` (2025, *IEEE Transactions on Cybernetics*): Y. Jiang, Q. Wang, G. Chen, and Z. Wu — Sliding Mode Fault-Tolerant Control for Nonlinear High-Order Fully Actuated Systems | DOI: `10.1109/TCYB.2024.3482320`
- `[S4]` `J2024_038` (2024, *IEEE Transactions on Cybernetics*): X. Liu, M. Chen, D. Zhou, and L. Sheng — Fault-Tolerant Control of Stochastic High-Order Fully Actuated Systems | DOI: `10.1109/TCYB.2023.3320441`
- `[S4]` `J2024_039` (2024, *IEEE Transactions on Cybernetics*): M. Cai, X. He, and D. Zhou — Finite-Time Fault-Tolerant Control via Fully Actuated System Approaches | DOI: `10.1109/TCYB.2024.3378208`
- `[S4]` `J2024_042` (2024, *IEEE Transactions on Circuits and Systems I: Regular Papers*): Y. Lu, K. Zhang, and B. Jiang — Fully Actuated System Approach Based Prescribed-Time Fault-Tolerant Formation Control for Unmanned Helicopters Under Fixed and Switching Topologies | DOI: `10.1109/TCSI.2024.3399779`
- `[S4]` `J2024_061` (2024, *Aerospace Science and Technology*): Q. Miao, K. Zhang, and B. Jinag — Incremental fully actuated system approach-based prescribed-time fault-tolerant formation control of helicopters under multiple faults | DOI: `10.1016/j.ast.2024.109334`
- `[S4]` `J2024_065` (2024, *IEEE Transactions on Cybernetics*): Y. Ma, K. Zhang, and B. Jiang — Neuroadaptive Cooperative Fault-Tolerant Control of Heterogeneous Multiagent Systems Based on Fully Actuated System Approaches | DOI: `10.1109/TCYB.2023.3318254`
- `[S4]` `J2024_074` (2024, *IEEE Transactions on Aerospace and Electronic Systems*): Q. Liu, K. Zhang, B. Jiang, and J. Xu — Prescribed-Time Fault-Tolerant Formation Control for Collision-Free Unmanned Helicopters: A High-Order Fully Actuated System Approach | DOI: `10.1109/TAES.2024.3382619`
- `[S4]` `J2024_089` (2024, *IEEE Transactions on Cybernetics*): M. Cai, X. He, and D. Zhou — Self-Healing Fault-Tolerant Control for High-Order Fully Actuated Systems Against Sensor Faults: A Redundancy Framework | DOI: `10.1109/TCYB.2023.3285903`
- `[S4]` `J2024_101` (2024, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): M. Cai, X. He, and D. Zhou — Unknown Nonaffine High-Order Fully Actuated Systems: Trajectory Tracking and Fault Tolerance | DOI: `10.1109/TSMC.2024.3373400`
- `[S4]` `J2023_026` (2023, *IEEE Transactions on Systems, Man, and Cybernetics: Systems*): M. Cai, X. He, and D. Zhou — Low-Power Fault-Tolerant Control for Nonideal High-Order Fully Actuated Systems | DOI: `10.1109/TSMC.2023.3257315`
- `[S4]` `J2023_033` (2023, *IEEE Transactions on Aerospace and Electronic Systems*): Y. Ma, K. Zhang, and B. Jiang — Prescribed-Time Fault-Tolerant Control for Fully Actuated Heterogeneous Multiagent Systems: A Hierarchical Design Approach | DOI: `10.1109/TAES.2023.3280895`
- `[S3]` `J2026_050` (2026, *International Journal of Robust and Nonlinear Control*): R. Li, X. Huo, W. Liu, K. Ma, and R. Ji — Adaptive Fuzzy Secure Consensus Control of Switched Filter-Based High-Order Fully Actuated MASs Under DoS Attacks | DOI: `10.1002/rnc.70680`
- `[S3]` `J2026_058` (2026, *ISA Transactions*): H. Li, S. Wang, H. Shi, L. Wang, and P. Li — Two-dimensional iterative learning fault-tolerant control for batch processes via a high-order fully actuated approach | DOI: `10.1016/j.isatra.2026.04.026`
- `[S3]` `J2026_063` (2026, *International Journal of Fuzzy Systems*): K. Liu, J. Li, and M. Liu — Fuzzy Neuro-adaptive Observer-Based Fault-Tolerant Control for Flexible Spacecraft Attitude Maneuver with Pointing Constraints | DOI: `10.1007/s40815-025-02028-7`
- `[S3]` `J2026_066` (2026, *International Journal of Systems Science*): K. Liu and Y. Cui — Fixed-time adaptive fuzzy fault-tolerant control for high-order nonlinear strict-feedback systems: a fully actuated system approach | DOI: `10.1080/00207721.2026.2640480`
- `[S3]` `J2026_074` (2026, *Acta Aeronautica et Astronautica Sinica (航空学报)*): Y. Lu, K. Zhang, and B. Jiang — Hierarchical fault-tolerant formation control for unmanned helicopters based on fully-actuated system approach
- `[S3]` `J2026_079` (2026, *IEEE Transactions on Vehicular Technology*): B. Meng, K. Zhang, B. Jiang, and L. Guo — Fully Actuated System Approach-Based Prescribed Time Fault-Tolerant Control and Hierarchical Structure Avoidance Collision for Multiple Unmanned Helicopters | DOI: `10.1109/TVT.2026.3663621`
- `[S3]` `J2026_081` (2026, *Control Engineering Practice*): B. Meng, K. Zhang, and B. Jiang — Hierarchical structure-based adaptive fault-tolerant control and collision avoidance for multiple fixed-wing UAVs: A fully actuated system approach | DOI: `10.1016/j.conengprac.2026.106763`
- `[S3]` `J2026_102` (2026, *Control Engineering Practice*): T. Wang, H. Liu, H. Kong, and G.-R. Duan — A fully actuated system approach to event-triggered fault-tolerant control of a class of interconnected nonlinear systems | DOI: `10.1016/j.conengprac.2026.106832`
- `[S3]` `J2026_119` (2026, *Applied Mathematics and Computation*): X. Wu and W. Sun — Adaptive fault tolerant optimal control for high-order fully actuated system and its application in spacecraft attitude tracking using reinforcement learning | DOI: `10.1016/j.amc.2025.129774`
- `[S3]` `J2026_148` (2026, *Nonlinear Dynamics*): J. Zhang, Y. Liu, Y. Duan, W. Li, and B. Zhang — Dynamic Event-Triggered Fault-Tolerant Tracking Control for Fully Actuated Strict-Feedback Systems | DOI: `10.1007/s11071-026-12247-8`
- `[S3]` `J2025_044` (2025, *International Journal of Robust and Nonlinear Control*): C. He, R. Qi, and B. Jiang — Fixed-Time Fault-Tolerant Control of a High-Order Fully Actuated System Under Actuator Faults and Uncertain Parameters | DOI: `10.1002/rnc.8046`
- `[S3]` `J2025_046` (2025, *Nonlinear Dynamics*): Z. Zhang, J. Chen, C. Chen, G. Zheng, Z. Song, and Y. Chen — Fixed-time fault-tolerant attitude consensus control for multiple spacecraft via fully actuated system approaches | DOI: `10.1007/s11071-025-11598-y`
- `[S3]` `J2025_047` (2025, *Applied Mathematical Modelling*): Y. Lu, K. Zhang, L. Shen, and J. Xia — Fixed-time fault-tolerant formation-containment control for unmanned helicopters via a fully actuated system approach | DOI: `10.1016/j.apm.2025.116004`
- `[S3]` `J2025_051` (2025, *Nonlinear Dynamics*): B. Meng, L. Shen, K. Zhang, and J. Xia — Fully actuated system approach-based fault-tolerant formation reconstruction control and optimal task assignment for fixed-wing UAVs | DOI: `10.1007/s11071-024-10246-1`
- `[S3]` `J2025_064` (2025, *ISA Transactions*): Q. Huang, J. Sun, and M. Zhao — Hybrid impulsive control for global stabilization of subfully actuated systems | DOI: `10.1016/j.isatra.2024.11.034`
- `[S3]` `J2025_079` (2025, *International Journal of Systems Science*): G. Liu, J. Xia, Q. Miao, B. Jiang, and K. Zhang — Neural-based fault-tolerant control using fully actuated system approach and intelligent safe planning for helicopter formation | DOI: `10.1080/00207721.2025.2511205`
- `[S3]` `J2025_100` (2025, *Control Engineering Practice*): N. Zhang, Q. Lin, and Z. Jiang — Robust trajectory tracking and fault-tolerant control for hyperbaric oxygen chambers based on High-order Fully Actuated System approaches | DOI: `10.1016/j.conengprac.2025.106554`
- `[S3]` `J2024_075` (2024, *International Journal of Systems Science*): M. Li, K. Zhang, Y. Ma, and B. Jiang — Prescribed-time fault-tolerant control for the formation of quadrotors based on fully-actuated system approaches | DOI: `10.1080/00207721.2024.2305306`
- `[S3]` `J2024_083` (2024, *International Journal of Systems Science*): M. Gong, L. Sheng, and D. Zhou — Robust fault-tolerant stabilisation of uncertain high-order fully actuated systems with actuator faults | DOI: `10.1080/00207721.2024.2312868`
- `[S3]` `J2023_001` (2023, *International Journal of Fuzzy Systems*): Y. Cui, G. Duan, X. Liu, and H. Zheng — Adaptive Fuzzy Fault-Tolerant Control of High-Order Nonlinear Systems: A Fully Actuated System Approach | DOI: `10.1007/s40815-023-01475-4`
- `[S3]` `J2023_009` (2023, *Journal of the Franklin Institute*): R. Dong, C. Hua, K. Li, and R. Meng — Adaptive fault-tolerant control for high-order fully actuated system with full-state constraints | DOI: `10.1016/j.jfranklin.2023.05.010`
- `[S3]` `J2023_019` (2023, *Journal of the Franklin Institute*): M. Cai, X. He, and D. Zhou — Fault-tolerant tracking control for nonlinear observer-extended high-order fully-actuated systems | DOI: `10.1016/j.jfranklin.2022.11.025`
- `[S3]` `J2022_007` (2022, *Neurocomputing*): X. Liu, M. Chen, L. Sheng, and D. Zhou — Adaptive fault-tolerant control for nonlinear high-order fully-actuated systems | DOI: `10.1016/j.neucom.2022.04.129`
