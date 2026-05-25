import { useEffect, useRef, useState } from "react";

/* Contador animado para os stats */
function CountUp({ target, suffix = "", duration = 1800 }) {
  const [value, setValue] = useState(0);
  const ref = useRef(null);
  const started = useRef(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !started.current) {
          started.current = true;
          const isPlus = String(target).startsWith("+");
          const num = parseInt(String(target).replace(/\D/g, ""), 10);
          const startTime = performance.now();
          const tick = (now) => {
            const progress = Math.min((now - startTime) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.round(eased * num);
            setValue((isPlus ? "+" : "") + current + suffix);
            if (progress < 1) requestAnimationFrame(tick);
          };
          requestAnimationFrame(tick);
        }
      },
      { threshold: 0.5 }
    );
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [target, duration, suffix]);

  return <span ref={ref}>{value || (String(target).startsWith("+") ? "+0" : "0" + suffix)}</span>;
}

function Hero() {
  const heroRef = useRef(null);

  useEffect(() => {
    const elements = heroRef.current?.querySelectorAll(".reveal");
    elements?.forEach((el, i) => {
      el.style.animationDelay = `${i * 0.15}s`;
      el.classList.add("revealed");
    });
  }, []);

  return (
    <section
      ref={heroRef}
      style={{ position:"relative", minHeight:"100vh", display:"flex", alignItems:"center", justifyContent:"center", overflow:"hidden", background:"var(--bg-primary)" }}
    >
      {/* Glow blobs */}
      <div style={{ position:"absolute",top:0,right:0,width:"600px",height:"600px",borderRadius:"50%",opacity:0.2,background:"radial-gradient(circle,var(--accent-sage) 0%,transparent 70%)",transform:"translate(30%,-30%)",pointerEvents:"none" }} />
      <div style={{ position:"absolute",bottom:0,left:0,width:"400px",height:"400px",borderRadius:"50%",opacity:0.15,background:"radial-gradient(circle,var(--accent-blush) 0%,transparent 70%)",transform:"translate(-30%,30%)",pointerEvents:"none" }} />

      {/* Gráfico decorativo SVG — linha ascendente suave */}
      <svg
        viewBox="0 0 400 120"
        xmlns="http://www.w3.org/2000/svg"
        style={{ position:"absolute", bottom:"12%", right:"4%", width:"320px", opacity:0.12, pointerEvents:"none" }}
      >
        <polyline
          points="0,100 60,80 120,85 180,55 240,60 300,30 360,20 400,8"
          fill="none"
          stroke="var(--accent-sage)"
          strokeWidth="3"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <polygon
          points="0,100 60,80 120,85 180,55 240,60 300,30 360,20 400,8 400,120 0,120"
          fill="var(--accent-sage)"
          opacity="0.25"
        />
        {[[60,80],[180,55],[300,30],[400,8]].map(([x,y],i) => (
          <circle key={i} cx={x} cy={y} r="4" fill="var(--accent-sage)" opacity="0.7" />
        ))}
      </svg>

      {/* ── Ícones flutuantes ── */}

      {/* Cifrão (CORRIGIDO — path não espelhado) */}
      <svg className="float-anim" style={{ position:"absolute",top:"18%",left:"8%",width:"32px",opacity:0.28,animationDelay:"0s" }} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="12" cy="12" r="10" stroke="var(--accent-terracotta)" strokeWidth="1.5"/>
        {/* Traço vertical do cifrão */}
        <line x1="12" y1="6" x2="12" y2="7" stroke="var(--accent-terracotta)" strokeWidth="1.5" strokeLinecap="round"/>
        <line x1="12" y1="17" x2="12" y2="18" stroke="var(--accent-terracotta)" strokeWidth="1.5" strokeLinecap="round"/>
        {/* Corpo do S correto */}
        <path d="M14.5 8.5c0 0-1-1-2.5-1s-2.5 1-2.5 2 1 1.5 2.5 2 2.5 1 2.5 2-1 2-2.5 2-2.5-1-2.5-1" stroke="var(--accent-terracotta)" strokeWidth="1.5" strokeLinecap="round"/>
      </svg>

      {/* Gráfico de barras crescente */}
      <svg className="float-anim" style={{ position:"absolute",top:"15%",right:"12%",width:"30px",opacity:0.22,animationDelay:"1.2s" }} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="3" y="12" width="4" height="9" rx="1" stroke="var(--accent-sage)" strokeWidth="1.5"/>
        <rect x="10" y="7" width="4" height="14" rx="1" stroke="var(--accent-sage)" strokeWidth="1.5"/>
        <rect x="17" y="3" width="4" height="18" rx="1" stroke="var(--accent-sage)" strokeWidth="1.5"/>
      </svg>

      {/* Seta de tendência ascendente */}
      <svg className="float-anim" style={{ position:"absolute",bottom:"28%",left:"14%",width:"28px",opacity:0.22,animationDelay:"2s" }} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M3 17 L9 11 L13 15 L21 7" stroke="var(--accent-gold)" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>
        <path d="M16 7h5v5" stroke="var(--accent-gold)" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>

      {/* Porquinho */}
      <svg className="float-anim" style={{ position:"absolute",bottom:"22%",right:"9%",width:"30px",opacity:0.22,animationDelay:"0.7s" }} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M19 10c0 4-3.1 7-7 7s-7-3-7-7a7 7 0 0 1 14 0z" stroke="var(--accent-blush-dark)" strokeWidth="1.5"/>
        <path d="M19 10h2a1 1 0 0 1 1 1v1a1 1 0 0 1-1 1h-2" stroke="var(--accent-blush-dark)" strokeWidth="1.5" strokeLinecap="round"/>
        <circle cx="9" cy="9" r="1" fill="var(--accent-blush-dark)"/>
        <path d="M10 17v2M14 17v2" stroke="var(--accent-blush-dark)" strokeWidth="1.5" strokeLinecap="round"/>
        <path d="M11 6.5c0-.8.9-1.5 1.5-1.5" stroke="var(--accent-blush-dark)" strokeWidth="1.5" strokeLinecap="round"/>
      </svg>

      {/* Escudo / proteção — novo */}
      <svg className="float-anim" style={{ position:"absolute",top:"40%",left:"5%",width:"24px",opacity:0.18,animationDelay:"1.6s" }} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="var(--accent-sage)" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
        <path d="M9 12l2 2 4-4" stroke="var(--accent-sage)" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>

      {/* Folha / crescimento orgânico — novo */}
      <svg className="float-anim" style={{ position:"absolute",top:"55%",right:"6%",width:"22px",opacity:0.18,animationDelay:"2.5s" }} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 22V12" stroke="var(--accent-gold)" strokeWidth="1.5" strokeLinecap="round"/>
        <path d="M12 12C12 12 7 10 5 5c4 0 7 2 7 7z" stroke="var(--accent-gold)" strokeWidth="1.5" strokeLinejoin="round"/>
        <path d="M12 12C12 12 17 10 19 5c-4 0-7 2-7 7z" stroke="var(--accent-gold)" strokeWidth="1.5" strokeLinejoin="round"/>
      </svg>

      {/* Linha topo */}
      <div style={{ position:"absolute",top:0,left:"50%",width:"1px",height:"128px",opacity:0.3,background:"linear-gradient(to bottom,transparent,var(--text-muted))" }} />

      {/* Conteúdo */}
      <div style={{ position:"relative",zIndex:10,textAlign:"center",padding:"0 1.5rem",maxWidth:"680px",width:"100%",margin:"0 auto" }}>
        <p className="reveal" style={{ textTransform:"uppercase",letterSpacing:"8px",fontSize:"12px",fontWeight:500,marginBottom:"2rem",color:"var(--accent-sage)" }}>
          Curso Online de Finanças
        </p>

        <h1 className="reveal font-display" style={{ fontSize:"clamp(3.5rem,10vw,7rem)",fontWeight:300,lineHeight:0.9,marginBottom:"2rem",color:"var(--text-primary)" }}>
          Meu Primeiro
          <br />
          <em className="not-italic" style={{ fontWeight:600,background:"linear-gradient(135deg,var(--accent-terracotta) 0%,var(--accent-blush-dark) 100%)",WebkitBackgroundClip:"text",WebkitTextFillColor:"transparent",backgroundClip:"text" }}>
            Investimento
          </em>
        </h1>

        <p className="reveal" style={{ fontSize:"1.1rem",lineHeight:1.75,color:"var(--text-secondary)",fontWeight:300,maxWidth:"420px",margin:"0 auto 2.5rem auto" }}>
          Aprenda a cuidar do seu dinheiro e investir com{" "}
          <span style={{ color:"var(--accent-terracotta)" }}>segurança</span>,
          leveza e confiança.
        </p>

        <div className="reveal" style={{ display:"flex",flexWrap:"wrap",gap:"1rem",justifyContent:"center",marginBottom:"5rem" }}>
          <button className="btn-primary btn-shimmer" onClick={() => document.getElementById('pricing')?.scrollIntoView({ behavior:'smooth' })}>Quero Começar Agora</button>
          <button className="btn-secondary" onClick={() => document.getElementById('modulos')?.scrollIntoView({ behavior:'smooth' })}>Ver Conteúdo</button>
        </div>

        {/* Stats com CountUp */}
        <div className="reveal" style={{ display:"grid",gridTemplateColumns:"repeat(3,1fr)",gap:"2rem",maxWidth:"480px",margin:"0 auto",paddingTop:"2rem",borderTop:"1px solid var(--border-light)" }}>
          {[
            { target:"+500", suffix:"", l:"Alunas",   sub:"satisfeitas" },
            { target:"6",    suffix:"", l:"Módulos",  sub:"completos"   },
            { target:"100",  suffix:"%",l:"Online",   sub:"no seu ritmo" },
          ].map((s) => (
            <div key={s.l} className="stat-item">
              <span className="font-display" style={{ fontSize:"2.5rem",fontWeight:300,color:"var(--accent-terracotta)" }}>
                <CountUp target={s.target} suffix={s.suffix} />
              </span>
              <span style={{ display:"block",fontSize:"11px",textTransform:"uppercase",letterSpacing:"4px",marginTop:"0.4rem",color:"var(--text-primary)",fontWeight:500 }}>{s.l}</span>
              <span style={{ display:"block",fontSize:"11px",color:"var(--text-muted)",marginTop:"0.1rem" }}>{s.sub}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Scroll indicator */}
      <div style={{ position:"absolute",bottom:"2rem",left:"50%",transform:"translateX(-50%)",display:"flex",flexDirection:"column",alignItems:"center",gap:"0.5rem",opacity:0.5 }}>
        <span style={{ fontSize:"10px",textTransform:"uppercase",letterSpacing:"4px",color:"var(--text-muted)" }}>Scroll</span>
        <div className="scroll-line" style={{ width:"1px",height:"40px",background:"var(--text-muted)" }} />
      </div>
    </section>
  );
}

export default Hero;