import React from 'react';
import { createRoot } from 'react-dom/client';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import System from './System/system';
import './index.css';

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <DndProvider backend={HTML5Backend}>
      <Router>
          <Routes>
            <Route path='/' element={<System />} />
          </Routes>
      </Router>
    </DndProvider>
  </React.StrictMode>
);
