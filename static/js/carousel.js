window.carousel = ({ total }) => ({
  current: 0,
  visible: 1,
  pct: 100,
  total,

  dragging: false,
  startX: 0,
  dx: 0,
  t0: 0,
  v: 0,
  moved: false,

  init() {
    this.update();
    window.addEventListener("resize", () => this.update(), { passive: true });
  },

  update() {
    if (window.innerWidth < 640) { this.visible = 1; this.pct = 100; }
    else if (window.innerWidth < 1024) { this.visible = 2; this.pct = 50; }
    else { this.visible = 3; this.pct = 100 / 3; }

    const max = this.max();
    if (this.current > max) this.current = max;
  },

  max() { return Math.max(0, this.total - this.visible); },
  canPrev() { return this.current > 0; },
  canNext() { return this.current < this.max(); },

  prev() { if (this.canPrev()) this.current--; },
  next() { if (this.canNext()) this.current++; },
  go(i) { this.current = Math.min(Math.max(0, i), this.max()); },

  edgeResistance(px) {
    if ((this.current === 0 && px > 0) || (this.current === this.max() && px < 0)) return px * 0.35;
    return px;
  },

  get translate() {
    const base = -(this.current * this.pct);
    if (!this.dragging) return base;
    const w = this.$refs.viewport?.clientWidth || 1;
    return base + (this.edgeResistance(this.dx) / w) * 100;
  },

  getX(e) { return e.clientX ?? 0; },

  onDown(e) {
    this.dragging = true;
    this.moved = false;
    this.startX = this.getX(e);
    this.dx = 0;
    this.t0 = performance.now();
    this.v = 0;
    e.target?.setPointerCapture?.(e.pointerId);
  },

  onMove(e) {
    if (!this.dragging) return;
    const x = this.getX(e);
    this.dx = x - this.startX;
    this.moved = this.moved || Math.abs(this.dx) > 6;
    const dt = Math.max(1, performance.now() - this.t0);
    this.v = this.dx / dt;
  },

  onUp() {
    if (!this.dragging) return;
    const w = this.$refs.viewport?.clientWidth || 1;
    const threshold = Math.min(120, w * 0.18);
    const fastSwipe = Math.abs(this.v) > 0.6;

    if (this.dx <= -threshold || (fastSwipe && this.v < 0)) this.next();
    else if (this.dx >= threshold || (fastSwipe && this.v > 0)) this.prev();

    this.dragging = false;
    this.dx = 0;
    this.v = 0;
  },

  onClickCapture(e) {
    if (this.moved) { e.preventDefault(); e.stopPropagation(); }
  },
});
