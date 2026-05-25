const benefits = [
  {
    title: "Controle financeiro",
    desc: "Domine suas finanças com clareza e método.",
    icon: (
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M3 3v18h18" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
        <path d="M7 16l4-5 4 3 4-6" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>
    ),
  },
  {
    title: "Reserva de emergência",
    desc: "Construa sua segurança financeira passo a passo.",
    icon: (
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M19 10c0 4-3.1 7-7 7s-7-3-7-7a7 7 0 0 1 14 0z" stroke="currentColor" strokeWidth="1.5"/>
        <path d="M19 10h2a1 1 0 0 1 1 1v1a1 1 0 0 1-1 1h-2" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
        <circle cx="9" cy="9" r="1" fill="currentColor"/>
        <path d="M10 17v2M14 17v2" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
        <path d="M11 6.5c0-.8.9-1.5 1.5-1.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
      </svg>
    ),
  },
  {
    title: "Primeiros investimentos",
    desc: "Dê o primeiro passo com confiança e segurança.",
    icon: (
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="1.5"/>
        <path d="M12 6v1m0 10v1M9 9.5c0-1.1.9-2 2-2h2a2 2 0 1 1 0 4h-2a2 2 0 1 0 0 4h2a2 2 0 0 0 2-2" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
      </svg>
    ),
  },
  {
    title: "Mentalidade financeira",
    desc: "Transforme sua relação com o dinheiro para sempre.",
    icon: (
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 3C7 3 3 7 3 12s4 9 9 9 9-4 9-9" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
        <path d="M16 3l2 2-6 6" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
        <path d="M18 3h3v3" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>
    ),
  },
];

function Benefits() {
  return (
    <section style={{ padding:"4rem 1.5rem 5rem", background:"var(--bg-secondary)" }}>
      <div style={{ maxWidth:"900px", margin:"0 auto", textAlign:"center" }}>

        <div style={{ display:"flex",alignItems:"center",justifyContent:"center",gap:"1rem",marginBottom:"1.5rem" }}>
          <div style={{ width:"40px",height:"1px",background:"var(--accent-sage)",flexShrink:0 }} />
          <p style={{ textTransform:"uppercase",letterSpacing:"6px",fontSize:"11px",fontWeight:500,color:"var(--accent-sage)" }}>O que você aprende</p>
          <div style={{ width:"40px",height:"1px",background:"var(--accent-sage)",flexShrink:0 }} />
        </div>

        <h2 className="font-display" style={{ fontSize:"clamp(2.5rem,6vw,4rem)",fontWeight:300,lineHeight:1.1,marginBottom:"4rem",color:"var(--text-primary)" }}>
          Uma nova relação
          <br />
          <em className="not-italic" style={{ fontWeight:600,color:"var(--accent-terracotta)" }}>com o dinheiro</em>
        </h2>

        <div style={{ display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(200px,1fr))",gap:"1.25rem" }}>
          {benefits.map((item, index) => (
            <div key={index} className="benefit-card group" style={{ textAlign:"left",animationDelay:`${index*0.1}s` }}>
              <span style={{ display:"block",marginBottom:"1.25rem",color:"var(--accent-terracotta)",transition:"transform 0.4s ease" }}
                onMouseEnter={e => e.currentTarget.style.transform="scale(1.15)"}
                onMouseLeave={e => e.currentTarget.style.transform="scale(1)"}
              >
                {item.icon}
              </span>
              <h3 className="font-display" style={{ fontSize:"1.1rem",fontWeight:500,marginBottom:"0.5rem",lineHeight:1.3,color:"var(--text-primary)" }}>
                {item.title}
              </h3>
              <p style={{ fontSize:"0.875rem",lineHeight:1.6,color:"var(--text-muted)" }}>
                {item.desc}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Benefits;