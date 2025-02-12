import { useState } from "react";

const Tooltip = ({ content, children }: { content: JSX.Element, children: JSX.Element }) => {
    const [visible, setVisible] = useState(false);

    return (
        <div className="relative inline-block">
            {children}
            <span
                className="tooltip-trigger ml-1 cursor-pointer"
                onMouseEnter={() => setVisible(true)}
                onMouseLeave={() => setVisible(false)}
                onClick={() => setVisible(!visible)}
            >
                &#9432;
            </span>
            {visible && (
                <div className="absolute left-0 mt-2 w-64 p-2 bg-gray-700 text-white text-sm rounded shadow-lg z-10">
                    {content}
                </div>
            )}
        </div>
    );
};

const gateFeatures = [
    {
        name: "Higher energy states (resonator)", // name of the feature
        qccsw: "3.1.0", // first version of QCCSW supporting the feature
        qiskit: {
            tutorial: "https://www.iqmacademy.com/notebookViewer/?path=/notebooks/iqm/deneb/Deneb_Unlocked_Resonator.ipynb"
        }, // Qiskit tutorial link or true if supported
        cirq: {
            tutorial: "https://iqm-finland.github.io/iqm-client/api/iqm.iqm_client.models.CircuitCompilationOptions.html#iqm.iqm_client.models.CircuitCompilationOptions.move_gate_validation"
        },
    },
    {
        name: "Mid-circuit measurements",
        qccsw: "3.1.0",
        qiskit: true,
        qrisp: true,
        cirq: true,
        cudaq: true,
    },
    {
        name: "Multiplexed measurements",
        qccsw: "1.0.0",
        qiskit: {
            tutorial: "https://iqm-finland.github.io/qiskit-on-iqm/user_guide.html#multiplexed-measurements"
        },
        cirq: {}
    },
    {
        name: "Classically controlled gates",
        qccsw: "3.1.0",
        qiskit: true,
        qrisp: true,
        cirq: false,
        cudaq: true,
    },
    {
        name: <Tooltip content={"Increase throughput by batching circuits that all read out the same qubits."}>Batched execution </Tooltip>,

        qccsw: "1.0.0",
        qiskit: true,
        cirq: true,
        cudaq: true,
        qrisp: true,
    },
    {
        name: "Dynamical decoupling",
        qccsw: "3.3.0",
        qiskit: {
            tutorial: "https://iqm-finland.github.io/iqm-client/api/iqm.iqm_client.models.CircuitCompilationOptions.html"
        },
        cirq: {
            tutorial: "https://iqm-finland.github.io/iqm-client/api/iqm.iqm_client.models.CircuitCompilationOptions.html"
        },
        cudaq: "-",
    },
    {
        name: <div style={{ display: "flex" }}> <Tooltip content={"Using a secondary detection event to confirm the successful preparation or measurement of a quantum state."
        }> Heralding</Tooltip></div>
        , qccsw: "1.0.0",
        qiskit: {
            tutorial: "https://iqm-finland.github.io/iqm-client/api/iqm.iqm_client.models.CircuitCompilationOptions.html#iqm.iqm_client.models.CircuitCompilationOptions.heralding_mode"
        },
        cirq: {
            tutorial: "https://iqm-finland.github.io/iqm-client/api/iqm.iqm_client.models.CircuitCompilationOptions.html#iqm.iqm_client.models.CircuitCompilationOptions.heralding_mode"
        },
    },
    {
        name: "Benchmarking tools",
        qccsw: "-",
        qiskit: {
            tutorial: "https://iqm-finland.github.io/qiskit-on-iqm/user_guide.html#benchmarking"
        }
    },
    {
        name: "Simulated backend",
        qccsw: "-",
        qiskit: true,
        cirq: "-",
        cudaq: "-",
        qrisp: "-",
    },
    {
        name: "Compilation check",
        qccsw: "1.0.0",
        qiskit: {
            tutorial: "https://www.iqmacademy.com/notebookViewer/?path=/notebooks/iqm/garnet/GarnetAlgorithmsChecker.ipynb"
        },
        cirq: true,
        cudaq: true,
        qrisp: true,
    },
    {
        name: "Resetting qubits",
        qccsw: "3.2.0",
        qiskit: {
            tutorial: "https://iqm-finland.github.io/qiskit-on-iqm/user_guide.html#resetting-qubits"
        },
        cirq: false,
        cudaq: false,
        qrisp: true,
    },
    {
        name: <Tooltip content="The qubits are actively reset once more using conditional pulses feedback loop before circuit execution.">Automated active reset</Tooltip>,
        qccsw: "3.3.0",
        qiskit: {
            tutorial: "https://iqm-finland.github.io/iqm-client/api/iqm.iqm_client.models.CircuitCompilationOptions.html#iqm.iqm_client.models.CircuitCompilationOptions.active_reset_cycles"
        },
        cirq: {
            tutorial: "https://iqm-finland.github.io/iqm-client/api/iqm.iqm_client.models.CircuitCompilationOptions.html#iqm.iqm_client.models.CircuitCompilationOptions.active_reset_cycles"
        },
    },
    {
        name: "Programmatically retrieve calibration data (Resonance)",
        qccsw: "-",
        qiskit: {
            tutorial: "https://www.iqmacademy.com/notebookViewer/?path=/notebooks/iqm/general/RetrieveCalibrationData.ipynb"
        },
        cirq: {
            tutorial: "https://www.iqmacademy.com/notebookViewer/?path=/notebooks/iqm/general/RetrieveCalibrationData.ipynb"
        },
        cudaq: {
            tutorial: "https://www.iqmacademy.com/notebookViewer/?path=/notebooks/iqm/general/RetrieveCalibrationData.ipynb"
        },
        qrisp: {
            tutorial: "https://www.iqmacademy.com/notebookViewer/?path=/notebooks/iqm/general/RetrieveCalibrationData.ipynb"
        },
    },
    {
        name: "Programmatically retrieve calibration data",
        qccsw: "-",
        qiskit: true,
        cirq: true,
        cudaq: true,
        qrisp: true,
    },
    {
        name: "MOVE operation support",
        qccsw: "3.0.0",
        qiskit: {
            tutorial: "https://www.iqmacademy.com/learn/deneb/01-move/"
        },
        cirq: {
            tutorial: "https://www.iqmacademy.com/learn/deneb/01-move/"
        }
    },
]

const pulseFeatures = [
    {
        name: "Ready-made experiments",
        resonance: false,
        onprem: true,
    },
    {
        name: "Custom calibrations",
        resonance: "Coming soon",
        onprem: true,
    },
    {
        name: "Custom gates",
        resonance: "Coming soon",
        onprem: true,
    },
    {
        name: "Pulse Schedule viewer",
        resonance: "Coming soon",
        onprem: true,
    },
    {
        name: "Custom compiler stages",
        resonance: "Coming soon",
        onprem: true,
    }
]

export { gateFeatures, pulseFeatures, Tooltip };