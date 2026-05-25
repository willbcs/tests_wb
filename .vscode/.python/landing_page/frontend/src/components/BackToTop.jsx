import { useState, useEffect } from "react";

function BackToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > window.innerHeight * 0.8);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const scrollToTop = () => window.scrollTo({ top: 0, behavior: "smooth" });

  return (
    <button
      onClick={scrollToTop}
      title="Voltar ao início"
      style={{
        position: "fixed",
        top: "1.25rem",
        right: "1.5rem",
        zIndex: 9999,
        display: "flex",
        alignItems: "center",
        gap: "0.6rem",
        padding: "0.85rem 1.75rem",
        borderRadius: "16px",
        border: "none",
        background: "var(--accent-terracotta)",
        color: "#fff",
        fontSize: "15px",
        fontFamily: "'DM Sans', sans-serif",
        fontWeight: 500,
        letterSpacing: "0.03em",
        cursor: "pointer",
        boxShadow: "0 12px 32px rgba(192, 112, 85, 0.35)",
        opacity: visible ? 1 : 0,
        transform: visible ? "translateY(0)" : "translateY(-16px)",
        pointerEvents: visible ? "auto" : "none",
        transition: "opacity 0.4s ease, transform 0.4s ease, box-shadow 0.3s ease",
      }}
      onMouseEnter={e => {
        e.currentTarget.style.boxShadow = "0 16px 40px rgba(192, 112, 85, 0.45)";
        e.currentTarget.style.transform = "translateY(2px)";
      }}
      onMouseLeave={e => {
        e.currentTarget.style.boxShadow = "0 12px 32px rgba(192, 112, 85, 0.35)";
        e.currentTarget.style.transform = "translateY(0)";
      }}
    >
      <svg width="14" height="14" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ flexShrink: 0 }}>
        <path d="M6 10V2M6 2L2 6M6 2L10 6" stroke="white" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      Voltar ao início
    </button>
  );
}

export default BackToTop;