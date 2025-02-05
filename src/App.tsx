import { useState, useEffect } from 'react';
import Fuse from 'fuse.js';
import { Search, X } from 'lucide-react';
import AppSwitcher from './AppSwitcher';
import docs from "../search.json";

interface Doc {
  title: string;
  package: string;
  description: string;
  url: string;
}


function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Doc[]>(docs);

  const fuse = new Fuse(docs, {
    keys: ['title', 'description', 'package'],
    threshold: 0.4
  });

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Check for CMD+K (Mac) or CTRL+K (Windows/Linux)
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setIsModalOpen(true);
      }
      // Close modal on ESC
      if (e.key === 'Escape') {
        setIsModalOpen(false);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  useEffect(() => {
    if (searchQuery) {
      const results = fuse.search(searchQuery);
      setSearchResults(results.map(result => result.item));
    } else {
      setSearchResults(docs);
    }
  }, [searchQuery]);

  const handleSearchClick = () => {
    setIsModalOpen(true);
  };

  const [isDocumentationSelected, setIsDocumentationSelected] = useState(true);


  const docLinks = [
    { href: "./iqm-pulse", title: "IQM Pulse", description: "Interface and implementations for control pulses." },
    { href: "./iqm-pulla", title: "IQM Pulla", description: "Pulse-level access library for compiling quantum circuits." },
    { href: "./qiskit-on-iqm/", title: "Qiskit on IQM", description: "Qiskit adapter for IQM’s quantum computers." },
    { href: "./cirq-on-iqm/", title: "Cirq on IQM", description: "Cirq adapter for IQM’s quantum computers." },
    { href: "./iqm-benchmarks/", title: "IQM Benchmarks", description: "Quantum Characterization, Verification, and Validation (QCVV) tools for quantum computing." },
    { href: "./iqm-client/", title: "IQM Client", description: "Python client for remote access to quantum computers for circuit-level access." },
    { href: "./iqm-station-control-client", title: "IQM Station Control Client", description: "Python client for remote access to quantum computers for pulse-level access." },
    { href: "./iqm-exa-common", title: "IQM EXA Common", description: "Abstract interfaces, helpers, utility classes, etc." },
  ];

  return (
    <div className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">

        <div className="flex flex-col sm:flex-row mb-4">
          <AppSwitcher />


          <div className="flex gap-4">
            <button
              className="relative px-4 py-2 text-gray-500"
              onClick={() => setIsDocumentationSelected(true)}
            >
              Documentation
              <span className={`block h-1 ml-4 mr-4 ${isDocumentationSelected ? 'bg-green-500' : 'bg-transparent'} absolute bottom-0 left-0 right-0`}></span>
            </button>
            {/*<button
              className="relative px-4 py-2 text-gray-500"
              onClick={() => setIsDocumentationSelected(false)}
            >
              Features
              <span className={`block h-1 ml-4 mr-4 ${!isDocumentationSelected ? 'bg-green-500' : 'bg-transparent'} absolute bottom-0 left-0 right-0`}></span>
            </button>*/}
          </div>
        </div>

        <div
          onClick={handleSearchClick}
          className="mt-6 mb-6 flex items-center gap-2 p-3 bg-white border border-gray-200 rounded-lg cursor-pointer hover:border-gray-300 transition-colors"
        >
          <Search className="w-5 h-5 text-gray-400" />
          <span className="text-gray-500">Search all documentation... {navigator.userAgent.includes('Mac') ? "Press ⌘K" : "Press Ctrl+K"}</span>
        </div>
        {isDocumentationSelected ? (
          <>
          <p>Find below the documentation for IQM client-side libraries that can be used to connect to {" "}
            <a href="https://resonance.meetiqm.com" target="_blank">IQM Resonance</a> and any IQM on-premise quantum computer.
            </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
            {docLinks.map((doc, index) => (
              <a key={index} href={doc.href} target='_blank' className="p-6 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <h2 className="text-lg font-semibold text-gray-900">{doc.title}</h2>
                <p className="mt-2 text-sm text-gray-600">{doc.description}</p>
              </a>
            ))}
          </div>
          </>
        ) : (
          <h1>Feature List</h1> 
        )}

        {/* Modal */}
        {isModalOpen && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-start justify-center pt-[15vh] z-50">
            <div className="bg-white rounded-xl shadow-2xl w-full max-w-2xl max-h-[70vh] overflow-hidden">
              <div className="p-4 border-b border-gray-100 flex items-center gap-3">
                <Search className="w-5 h-5 text-gray-400" />
                <input
                  type="text"
                  autoFocus
                  placeholder="Search documentation..."
                  className="flex-1 outline-none text-gray-900"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
                <button
                  onClick={() => setIsModalOpen(false)}
                  className="p-1 hover:bg-gray-100 rounded-md transition-colors"
                >
                  <X className="w-5 h-5 text-gray-500" />
                </button>
              </div>

              <div className="overflow-y-auto max-h-[calc(70vh-4rem)]">
                {searchResults.map((doc, index) => (
                  <a
                    key={index}
                    href={"." + doc.url}
                    target="_blank"
                    className="block p-4 hover:bg-gray-50 transition-colors overflow-hidden"
                  >
                    <h3 className="font-medium text-gray-900">{doc.title}</h3>
                    <span className="text-sm text-gray-500 block mt-1">
                      {doc.package}
                    </span>
                    <p className="text-sm text-gray-600 mt-1">
                      {doc.description}
                    </p>
                  </a>
                ))}
              </div>
            </div>
          </div>
        )}



        <footer className="mt-8 text-center text-sm text-gray-500 border-gray-300 border-t pt-4">
          <span>Copyright IQM Quantum Computers 2021-2025.</span>
          <br />
          <span>Need assistance? Contact us <a href="mailto:support@meetiqm.com">support@meetiqm.com</a></span>
        </footer>
      </div>
    </div>
  );
}

export default App;