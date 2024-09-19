import React from 'react';
import { Handle } from 'react-flow-renderer';

const CustomNode = ({ data }) => {
  let nodeStyle = {};
  
  return (
    <div className="custom-node" style={nodeStyle}>
      <Handle type="target" position="left" />
      <div className="node-header">{data.label}</div>
      <Handle type="source" position="right" />
    </div>
  );
};

export default CustomNode;