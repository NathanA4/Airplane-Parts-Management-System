import React from 'react';
import { createRoot } from 'react-dom/client';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import System from './System/system';
import Login from './login/login';
import Register from './login/register';
import ViewPlane from './ViewPlane/viewplane';
import Home from './Home/home';
import './index.css';

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <DndProvider backend={HTML5Backend}>
      <Router>
          <Routes>
            <Route path='/' element={<Home/>}/>
            <Route path='register' element={<Register/>}/>
            <Route path='Login' element={<Login/>}/>
            <Route path='systems' element={<System />} />
            <Route path='viewplane' element={<ViewPlane/>}/> 
          </Routes>
      </Router>
    </DndProvider>
  </React.StrictMode>
);
