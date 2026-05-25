import Hero from "./components/Hero";
import TrustBar from "./components/TrustBar";
import Benefits from "./components/Benefits";
import Modules from "./components/Modules";
import Testimonials from "./components/Testimonials";
import Pricing from "./components/Pricing";
import FAQ from "./components/FAQ";
import Footer from "./components/Footer";
import BackToTop from "./components/BackToTop";
import "./App.css";

function App() {
  return (
    <div>
      <BackToTop />
      <Hero />
      <TrustBar />
      <Benefits />
      <Modules />
      <Testimonials />
      <Pricing />
      <FAQ />
      <Footer />
    </div>
  );
}

export default App;