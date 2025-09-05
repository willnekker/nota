import React from 'react';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Header */}
      <header className="bg-white shadow p-4">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-800">Nota Dashboard</h1>
          {/* Navigation or User Info */}
          <nav>
            <ul className="flex space-x-4">
              <li><a href="#" className="text-blue-600 hover:underline">Courses</a></li>
              <li><a href="#" className="text-blue-600 hover:underline">Assignments</a></li>
              <li><a href="#" className="text-blue-600 hover:underline">Summaries</a></li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow container mx-auto p-4">
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold text-gray-700 mb-4">Welcome to your Canvas LMS Assistant!</h2>
          <p className="text-gray-600">This is where your course data, assignments, and summaries will appear.</p>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-white p-4 text-center">
        <p>&copy; 2023 Nota. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;