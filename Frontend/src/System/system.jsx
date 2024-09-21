import React, { useState, useCallback, useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import ReactFlow, {
  addEdge,
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
} from 'react-flow-renderer';
import CustomNode from './node.jsx';
import { parameter } from './partparameter.js';
import './system.css';
import 'reactjs-popup/dist/index.css';
import LandingGearImage from '../assets/LandingGear.png'
import EngineImage from '../assets/Engine.png';
import FuelSystemImage from '../assets/FuelSystem.png';
import CockpitControlsImage from '../assets/CockpitControls.png'
import AvionicsImage from '../assets/Avionics.jpg'
import ElectricalSystemImage from '../assets/ElectricalSystem.png'
import FlightInstrumentsImage from '../assets/FlightInstruments.webp'
import BrakesImage from '../assets/Brakes.png'
import ExhaustSystemImage from '../assets/ExhaustSystem.png'
import CoolingSystemImage from '../assets/CoolingSystem.png'
import PowerPlantImage from '../assets/PowerPlant.png'
import axios from 'axios'; 

const apiRoute = 'http://localhost:5000'; 

const initialNodes = [];
const initialEdges = [];

const nodeTypes = {
  customNode: CustomNode,
};

const components = {
  airplanePart: {
    physicalModel: [
      { name: 'Engine', imageUrl: EngineImage },
      { name: 'LandingGear', imageUrl: LandingGearImage },
      { name: 'FuelSystem', imageUrl: FuelSystemImage },
      { name: 'CockpitControls', imageUrl: CockpitControlsImage },
      { name: 'Avionics', imageUrl: AvionicsImage },
      { name: 'ElectricalSystem', imageUrl: ElectricalSystemImage },
      { name: 'FlightInstruments', imageUrl: FlightInstrumentsImage },
      { name: 'Brakes', imageUrl: BrakesImage },
      { name: 'ExhaustSystem', imageUrl: ExhaustSystemImage },
      { name: 'CoolingSystem', imageUrl: CoolingSystemImage },
      { name: 'Powerplant', imageUrl: PowerPlantImage }
    ]
  }
};

function System() {
  const navigate = useNavigate();
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const [contextMenu, setContextMenu] = useState({ visible: false, x: 0, y: 0, nodeId: null });
  const [selectedNode, setSelectedNode] = useState(null);
  const [open, setOpen] = useState(true); 
  const [userData, setUserData] = useState('');

  const handleSaveFormData = (userData) => {
    if (userData) {
      setUserData(userData);
      setOpen(false);
    }
  };

  const viewPlane = () => {
    navigate('/viewplane');
  };

  const renderCustomInput = (param, index) => {
    return(
      <input type="text" value={param.value} style={{borderColor: param.valid ? 'initial' : 'red'}} onChange={(e) => handleUpdateParameter(index, e.target.value)}/>
    );
  };

  useEffect(() => {
    setOpen(true);
  }, []);

  const onConnect = useCallback((params) => {
    setEdges((eds) => addEdge({ ...params }, eds));
  }, [setEdges]);

  const onDragOver = (event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  };

  const onDrop = (event) => {
    event.preventDefault();
  
    const reactFlowBounds = event.target.getBoundingClientRect();
    const type = event.dataTransfer.getData('application/reactflow');
    const position = {
      x: event.clientX - reactFlowBounds.left,
      y: event.clientY - reactFlowBounds.top,
    };
  
    let parameters = [];
    let imageUrl = '';
    let category = '';

    const part = components.airplanePart.physicalModel.find(p => p.name === type);

    if (part) {
      category = `physicalModel.${part.name}`;
      imageUrl = part.imageUrl;
      parameters = parameter.airplanePart.physicalModel[part.name].map(({name, type}) => ({ name, value: '', type, valid: true }));
    }

    const newNode = {
      id: (nodes.length + 1).toString(),
      type: 'customNode',
      position,
      data: { label: `${type}`, parameters, category },
      style: { border: '3px solid #858080', padding: '10px', borderRadius: '5px', backgroundColor: '#858080' },
    };
  
    setNodes((nds) => nds.concat(newNode));
  };

  const onDragStart = (event, nodeType) => {
    event.dataTransfer.setData('application/reactflow', nodeType);
    event.dataTransfer.effectAllowed = 'move';
  };

  const onNodeContextMenu = (event, node) => {
    event.preventDefault();
    setContextMenu({
      visible: true,
      x: event.clientX,
      y: event.clientY,
      nodeId: node.id,
    });
    setSelectedNode(node);
  };

  const handleCloseContextMenu = () => {
    setContextMenu({ visible: false, x: 0, y: 0, nodeId: null });
    setSelectedNode(null);
  };

  const handleUpdateParameter = (index, value) => {
    const updatedNodes = nodes.map((node) => {
      if (node.id === selectedNode.id) {
        const updatedParameters = [...node.data.parameters];
        const { type } = updatedParameters[index];
        let parsedValue = value;
        let valid = true;

        if (type === 'int') {
          parsedValue = parseInt(value, 10);
          valid = !isNaN(parsedValue);
        } else if (type === 'float') {
          parsedValue = parseFloat(value);
          valid = !isNaN(parsedValue);
        }

        updatedParameters[index].value = valid ? parsedValue : value;
        updatedParameters[index].valid = valid;
        return {
          ...node,
          data: {
            ...node.data,
            parameters: updatedParameters,
          },
        };
      }
      return node;
    });
    setNodes(updatedNodes);
  };

  const serializeData = () => {
    const serializedNodes = nodes.map((node) => ({
      id: node.id,
      type: node.data.category,
      name: node.data.label,
      parameters: node.data.parameters.map((param) => ({
        name: param.name,
        value: param.valid ? param.value : '',
        type: param.type,
      })),
    }));

    const serializedEdges = edges.map((edge) => ({
      source: edge.source,
      target: edge.target,
    }));

    return { nodes: serializedNodes, edges: serializedEdges };
  };

  const saveModel = () => {
    const serializedData = serializeData();
    console.log('Serialized Data:', JSON.stringify(serializedData, null, 2));
    console.log('Form Data:', userData);

    setSharedData({ nodes: serializedData.nodes, edges: serializedData.edges, userData});

    axios
      .post(`${apiRoute}/api/savemodel`, { ...serializedData, userData, userID: localStorage.getItem('userId') }) 
      .then((response) => {
        console.log('Response from server:', response.data);
      })
      .catch((error) => {
        console.error('Error sending data to server:', error);
      });
  };


  return (
    <div className="dndflow">
      <div className="sidebar">
      <h3 className="h3">AirPlane Parts</h3>
      {components.airplanePart.physicalModel.map(({ name, imageUrl }) => (
        <div
          key={name}
          className="dndnode parts"
          onDragStart={(event) => onDragStart(event, name)}
          draggable
        >
          <img src={imageUrl} alt={name} className="node-image" />
          <span>{name}</span>
        </div>
      ))}
      </div>

      <div className="main-content" onClick={handleCloseContextMenu}>
        <h1 className="h1">Build Internal Model:</h1>
        <div className="reactflow-wrapper" onDrop={onDrop} onDragOver={onDragOver}>
          <ReactFlow className="mini-map-black"
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            nodeTypes={nodeTypes}
            onNodeContextMenu={onNodeContextMenu}
            fitView
          >
            <MiniMap className="mini-map-black"/>
            <Controls />
            <Background />
          </ReactFlow>
        </div>
        <div className="section">
          <span className="text">!</span>
          <div className="popup">
            <p>Tips:</p>
            <ul>
              <li>Drag and drop airplane parts from the sidebar onto the main content area.</li>
              <li>Right-click a part to input parameters.</li>
              <li>Connect parts by dragging a line between them.</li>
              <li>Save your model.</li>
              <li>After saving the model, you can choose the airplane model/design.</li>
            </ul>
          </div>
        </div>
        <div className="">
          <button className="save-button" onClick={saveModel}>Save Model</button>
          <button className="view-button" onClick={viewPlane}>View AirPlane Body</button>
        </div>
      </div>
      {contextMenu.visible && (
        <div
          className="context-menu"
          style={{ top: contextMenu.y, left: contextMenu.x }}
        >
          <h4>{selectedNode?.data.label} Parameters</h4>
          {selectedNode && selectedNode.data.parameters && selectedNode.data.parameters.map((param, index) => (
            <div key={index}>
              <label>{param.name}: </label>
              {renderCustomInput(param, index)}
              {!param.valid && <span className="error-message">Invalid {param.type}</span>}
            </div>
          ))}
          <button onClick={handleCloseContextMenu}>Close</button>
        </div>
      )}
    </div>
  );
}

export default System;
