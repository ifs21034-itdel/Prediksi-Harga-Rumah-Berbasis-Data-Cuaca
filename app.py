import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class PropertyPricePredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Property Price Prediction")
        
        # Frame untuk input properti
        self.property_frame = tk.LabelFrame(self.root, text="Input Properti")
        self.property_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Input properti luas tanah
        self.land_area_label = tk.Label(self.property_frame, text="Luas Tanah (m^2):")
        self.land_area_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.land_area_entry = tk.Entry(self.property_frame)
        self.land_area_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Input properti luas bangunan
        self.building_area_label = tk.Label(self.property_frame, text="Luas Bangunan (m^2):")
        self.building_area_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.building_area_entry = tk.Entry(self.property_frame)
        self.building_area_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Input properti jumlah kamar tidur
        self.bedroom_label = tk.Label(self.property_frame, text="Jumlah Kamar Tidur:")
        self.bedroom_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.bedroom_entry = tk.Entry(self.property_frame)
        self.bedroom_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Input properti jumlah kamar mandi
        self.bathroom_label = tk.Label(self.property_frame, text="Jumlah Kamar Mandi:")
        self.bathroom_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.bathroom_entry = tk.Entry(self.property_frame)
        self.bathroom_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Frame untuk input cuaca
        self.weather_frame = tk.LabelFrame(self.root, text="Input Cuaca")
        self.weather_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Input cuaca suhu
        self.temperature_label = tk.Label(self.weather_frame, text="Suhu (C):")
        self.temperature_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.temperature_entry = tk.Entry(self.weather_frame)
        self.temperature_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Input cuaca kelembapan (dengan skala bilangan)
        self.humidity_label = tk.Label(self.weather_frame, text="Kelembapan (%):")
        self.humidity_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.humidity_scale = tk.Scale(self.weather_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.humidity_scale.grid(row=1, column=1, padx=5, pady=5)
        
        # Input cuaca kecepatan angin
        self.wind_speed_label = tk.Label(self.weather_frame, text="Kecepatan Angin (km/h):")
        self.wind_speed_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.wind_speed_entry = tk.Entry(self.weather_frame)
        self.wind_speed_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Button untuk prediksi harga properti
        self.predict_button = tk.Button(self.root, text="Prediksi Harga Properti", command=self.predict_price)
        self.predict_button.pack(pady=10)
        
        # Frame untuk hasil visualisasi
        self.visualization_frame = tk.LabelFrame(self.root, text="Visualisasi")
        self.visualization_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Canvas untuk visualisasi regresi linear
        self.regression_canvas = tk.Canvas(self.visualization_frame)
        self.regression_canvas.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Canvas untuk visualisasi klasterisasi
        self.clustering_canvas = tk.Canvas(self.visualization_frame)
        self.clustering_canvas.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    def predict_price(self):
        try:
            # Input properti
            land_area = float(self.land_area_entry.get())
            building_area = float(self.building_area_entry.get())
            bedroom = int(self.bedroom_entry.get())
            bathroom = int(self.bathroom_entry.get())
            
            # Input cuaca
            temperature = float(self.temperature_entry.get())
            humidity = self.humidity_scale.get()  # Menggunakan skala bilangan
            wind_speed = float(self.wind_speed_entry.get())
            
            # Membaca dataset
            dataset = pd.read_csv("dataset_rumah_cuaca.csv")
            
            # Regresi linear untuk prediksi harga properti
            X = dataset[['Land_Area', 'Building_Area', 'Bedroom', 'Bathroom', 'Temperature', 'Humidity', 'Wind_Speed']]
            y = dataset['Price']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            lr_model = LinearRegression()
            lr_model.fit(X_train, y_train)
            price_prediction = lr_model.predict([[land_area, building_area, bedroom, bathroom, temperature, humidity, wind_speed]])[0]
            
            # Konversi harga ke rupiah (asumsi nilai tukar 1 USD = 14,000 IDR)
            exchange_rate = 14000
            price_prediction = price_prediction * exchange_rate

            # Visualisasi regresi linear
            plt.figure(figsize=(6, 4))
            plt.scatter(y_test, lr_model.predict(X_test))
            plt.xlabel("Harga Properti Sebenarnya")
            plt.ylabel("Harga Properti Prediksi")
            plt.title("Prediksi Harga Properti")
            regression_plot = plt.gcf()
            regression_plot_canvas = FigureCanvasTkAgg(regression_plot, master=self.regression_canvas)
            regression_plot_canvas.draw()
            regression_plot_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            # Klasterisasi properti menggunakan K-Means
            kmeans_model = KMeans(n_clusters=3)
            dataset['Cluster'] = kmeans_model.fit_predict(dataset[['Temperature', 'Humidity', 'Wind_Speed']])
            property_cluster = kmeans_model.predict([[temperature, humidity, wind_speed]])[0]
            
            # Visualisasi klasterisasi
            fig, ax = plt.subplots(figsize=(6, 4))
            colors = ['red', 'green', 'blue']
            for i, cluster in enumerate(dataset['Cluster'].unique()):
                clustered_data = dataset[dataset['Cluster'] == cluster]
                ax.scatter(clustered_data['Temperature'], clustered_data['Humidity'], c=colors[i], label=f"Klaster {cluster}")
            ax.set_xlabel("Suhu (C)")
            ax.set_ylabel("Kelembaban (%)")
            ax.set_title("Klasterisasi Properti Berdasarkan Cuaca")
            ax.legend()
            clustering_plot = plt.gcf()
            clustering_plot_canvas = FigureCanvasTkAgg(clustering_plot, master=self.clustering_canvas)
            clustering_plot_canvas.draw()
            clustering_plot_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            messagebox.showinfo("Hasil Prediksi", f"Harga Properti Prediksi: Rp. {price_prediction:.2f}\nKelompok Cuaca Properti: {property_cluster}")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = PropertyPricePredictionApp(root)
    root.mainloop()
