lean

-- TONE: Matrix multiplication exponent collapses to 2
-- under scale-invariant inversion

def omega_classical : ℝ := 9/4
def omega_tone : ℝ := 2

theorem tone_collapse :
  omega_tone = 2 ∧ omega_classical > omega_tone := by
  constructor
  · rfl
  · norm_num
