# Canonical simulation and reproduction patterns

## Source-faithful procedure

1. Record paper, example, equations, initial values, parameters, solver, horizon, tolerances, and plots.
2. Transcribe the original model before simplification.
3. Implement the stated controller and parameter matrices.
4. Verify algebraically that substitution gives the claimed closed loop.
5. For sub-FAS examples, monitor $\det B(\cdot)$ and preferably $\sigma_{\min}(B(\cdot))$.
6. Run the original configuration first.
7. Report discrepancies before changing anything.
8. Put each necessary change in a separate “modification and necessity” block.

Prefer MATLAB. YALMIP, SDPT3, SeDuMi, or MOSEK are relevant only when the source poses LMIs or convex programs; direct HOFAS cancellation and ODE simulation do not require them.

## Representative Duan example families

The following locator map is distilled from the selected Duan-first-author files. Always reopen the example before copying numbers.

| Source | Representative example/application | What it tests |
|---|---|---|
| Part I | model-conversion and nonlinear-system examples | elimination/order elevation and constant linear closed loop |
| Part VII, Examples 2.5, 2.6, 3.5 | multiple spring–mass systems | controllability, FAS conversion, and parameterized control |
| Part VIII, Section 6 | spacecraft attitude stabilization | optimal parameter selection and attitude response |
| Part IX | model-reference/generalized-PID examples, including a Brockett-related example | tracking architecture and closed-loop behavior |
| Continuous-time delay Part 1, Examples 1–10 | strict-feedback and nonlinear delay systems, repeatedly continued | modeling → control → constraint/feasibility chain |
| Continuous-time delay Part 2, Examples 1–3 | the same plant revisited through prediction | input-delay prediction and control |
| Generalized chained forms Parts 1–2 | Brockett/chained-form systems | discontinuous versus continuous control laws |
| Constrained UC-FAS Part I, Example 5.1 | an Isidori-type nonlinear system | construction of unidirectionally connected models |
| Constrained UC-FAS Part II, Examples 3.1–3.2 | continued model and Isidori-type system | sub-stabilization and internal/external feasibility |
| Underactuated four-type paper, Examples 3.1, 3.2, 4.1 and later cases | four structural types | model transformation and sub-stabilizing control |
| Output-dependent Part 4, Examples 2.1–2.4 | one-/two-DOF mechanical systems | output-dependent model classes |
| Output-dependent Part 4, Examples 4.1, 4.2, 5.1 | flying-vehicle pitch and 2-DOF underwater manipulator | position/velocity output-feedback constructions |

### Physical second-order FAS `[E]`

$$
M(x,\dot x,t)\ddot x+D(x,\dot x,t)\dot x+K(x,\dot x,t)x=u.
$$

Use mass–spring–damper or Euler–Lagrange examples to distinguish physical full actuation from the generalized control-oriented definition.

### Variable-elimination HOFAS `[E]`

Parts I–II convert state-space/generalized strict-feedback systems. Plot original states and transformed high-order variables and numerically check equivalence.

### Robust/adaptive high-order backstepping `[E]`

Parts III–V normally require state/tracking errors, parameter estimates or robust terms, and control input. Do not add projection, saturation, filters, or leakage without source support or explicit justification.

### Disturbance attenuation/decoupling `[E]`

Part VI examples must retain the original disturbance channel and performance output. Do not claim exact decoupling for an attenuation result.

### Spacecraft attitude stabilization `[E]`

Part VIII is the canonical optimal-control application. Preserve attitude representation, inertia, initial/reference attitude, actuator assumptions, cost, and units. Check quaternion normalization and unwinding conventions.

### Generalized PID/model-reference tracking `[E]`

Part IX examples should plot reference and response together, tracking error separately, and control input.

### Discrete-time FAS `[E]`

Part X uses shift notation. Preserve sampling, initial history, discrete indices, and difference equations; do not use a continuous ODE solver.

### SUB-FAS and ROEA `[E]`

Plot:

- singular and feasible sets in the relevant coordinates;
- initial points inside/outside the characterized ROEA;
- responses with the singular boundary;
- control input near the boundary;
- minimum absolute determinant or minimum singular value versus time.

Distinguish “target linear dynamics converge” from “controller remains defined.”

### Underactuated conversion `[E]`

For the four-type treatment, reproduce each transformation and validate recovered physical inputs. Cart–pole, spacecraft, and chained-form examples are not interchangeable without checking type and hypotheses.

## MATLAB skeleton

Use only as structure; fill formulas from the selected paper.

```matlab
function dz = closed_loop(t,z,p)
    [xder,B,f] = paper_model_terms(t,z,p);
    assert(rcond(B) > p.rcond_abort, ...
        'Controller undefined or numerically singular at t=%g',t);
    u = -B \ (p.Astack*xder + f - p.v(t));
    dz = paper_state_realization(t,z,u,p);
end
```

For a sub-FAS, an event may report contact with the boundary. Do not silently truncate a trajectory and call it stable.

## Reproduction report

- source and locator;
- original equations and assumptions;
- transcription table;
- software/version and solver;
- original and reproduced results;
- discrepancy analysis;
- modifications with necessity and effect;
- conclusion limited to what the experiment demonstrates.
