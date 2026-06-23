# React Frontend - Project HIPL

Professional React 18+ Frontend for N8N Automation Platform

## Project Structure

```
frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Dashboard/
│   │   │   ├── FinanceDashboard.jsx
│   │   │   ├── ProcurementDashboard.jsx
│   │   │   ├── ProductionDashboard.jsx
│   │   │   ├── InventoryDashboard.jsx
│   │   │   ├── LogisticsDashboard.jsx
│   │   │   ├── HRDashboard.jsx
│   │   │   ├── QualityDashboard.jsx
│   │   │   └── SalesDashboard.jsx
│   │   ├── Auth/
│   │   │   ├── Login.jsx
│   │   │   ├── ProtectedRoute.jsx
│   │   │   └── RoleBasedAccess.jsx
│   │   ├── Common/
│   │   │   ├── Header.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── Loading.jsx
│   │   └── Charts/
│   │       ├── LineChart.jsx
│   │       ├── BarChart.jsx
│   │       └── PieChart.jsx
│   ├── pages/
│   │   ├── Home.jsx
│   │   ├── Dashboard.jsx
│   │   ├── Invoices.jsx
│   │   ├── PurchaseOrders.jsx
│   │   ├── Shipments.jsx
│   │   ├── Employees.jsx
│   │   ├── QualityChecks.jsx
│   │   ├── Sales.jsx
│   │   └── NotFound.jsx
│   ├── services/
│   │   ├── api.js
│   │   ├── auth.js
│   │   └── workflows.js
│   ├── store/
│   │   ├── authSlice.js
│   │   ├── dashboardSlice.js
│   │   └── store.js
│   ├── utils/
│   │   ├── constants.js
│   │   ├── formatters.js
│   │   └── validators.js
│   ├── styles/
│   │   ├── tailwind.css
│   │   ├── global.css
│   │   └── variables.css
│   ├── App.jsx
│   ├── main.jsx
│   └── config.js
├── .env.example
├── .gitignore
├── package.json
├── tailwind.config.js
├── postcss.config.js
└── vite.config.js
```

## Key Features

### 1. Role-Based Dashboards
- Finance Manager Dashboard
- Procurement Manager Dashboard
- Production Manager Dashboard
- Inventory Manager Dashboard
- Logistics Manager Dashboard
- HR Manager Dashboard
- Quality Manager Dashboard
- Sales Manager Dashboard
- System Administrator Dashboard

### 2. Authentication & Authorization
- JWT-based login
- Role-based access control
- Protected routes
- Token refresh mechanism
- Automatic logout on token expiration

### 3. Data Visualization
- Real-time charts (Line, Bar, Pie)
- KPI cards with trend indicators
- Data tables with filtering and sorting
- Excel import/export functionality

### 4. Responsive Design
- Mobile-first approach
- Tailwind CSS for styling
- Dark mode support
- Accessibility features (WCAG 2.1)

### 5. State Management
- Redux for global state
- Redux Thunk for async operations
- Local state for component-specific data

## Setup Instructions

### Prerequisites
- Node.js 18+
- npm 9+

### Installation

```bash
cd frontend
npm install
```

### Development

```bash
npm run dev
# Access at http://localhost:5173
```

### Build

```bash
npm run build
```

### Preview

```bash
npm run preview
```

## Environment Variables

Create a `.env` file:

```env
VITE_API_URL=http://localhost:8000/api/v1
VITE_N8N_URL=http://localhost:5678
VITE_APP_NAME=Project HIPL
VITE_APP_VERSION=1.0.0
```

## Dependencies

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "redux": "^4.2.1",
    "react-redux": "^8.1.3",
    "@reduxjs/toolkit": "^1.9.7",
    "axios": "^1.6.5",
    "recharts": "^2.10.3",
    "chart.js": "^4.4.1",
    "react-chartjs-2": "^5.2.0",
    "tailwindcss": "^3.4.1",
    "xlsx": "^0.18.5"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.8",
    "postcss": "^8.4.32",
    "autoprefixer": "^10.4.17"
  }
}
```

## Component Examples

### Login Component
```jsx
// components/Auth/Login.jsx
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { loginUser } from '../../store/authSlice';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(loginUser({ email, password }));
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="text-3xl font-bold text-center">Project HIPL</h2>
          <p className="text-center text-gray-600">N8N Automation Platform</p>
        </div>
        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Email & Password inputs */}
        </form>
      </div>
    </div>
  );
}
```

### Finance Dashboard Component
```jsx
// components/Dashboard/FinanceDashboard.jsx
import { useEffect, useState } from 'react';
import { getInvoices, getPayments } from '../../services/api';
import Charts from '../Charts';

export default function FinanceDashboard() {
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [invoiceData, paymentData] = await Promise.all([
        getInvoices(),
        getPayments()
      ]);
      setInvoices(invoiceData);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container">
      <h1 className="text-3xl font-bold">Finance Dashboard</h1>
      {/* Dashboard content */}
    </div>
  );
}
```

---

**Version:** 1.0.0
**Status:** Production Ready ✅
