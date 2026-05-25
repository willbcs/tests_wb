function Footer() {
  return (
    <footer style={{ background: "var(--bg-primary)", borderTop: "1px solid var(--border-light)", padding: "1.0rem 1.0rem" }}>
      <div style={{ maxWidth: "1000px", margin: "0 auto", display: "flex", flexDirection: "column", alignItems: "center", gap: "0.5rem", textAlign: "center" }}>
        <p className="font-display" style={{ fontSize: "1.1rem", fontWeight: 300, color: "var(--text-primary)" }}>
          Meu Primeiro{" "}
          <em className="not-italic" style={{ fontWeight: 600, color: "var(--accent-terracotta)" }}>Investimento</em>
        </p>
        <p style={{ fontSize: "11px", textTransform: "uppercase", letterSpacing: "4px", color: "var(--text-muted)" }}>
          © 2026 · Todos os direitos reservados
        </p>
      </div>
    </footer>
  );
}

export default Footer;
