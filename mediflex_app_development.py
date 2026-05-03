from google import genai
from google.genai import types
import base64
import os

def generate():
  client = genai.Client(
      vertexai=True,
      api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"),
  )

  msg1_text1 = types.Part.from_text(text="""1. Resumen de Funciones de la WebAppLa plataforma está diseñada como un centro de control profesional para clínicas, con las siguientes funciones principales:Panel de Control Responsive: Una interfaz moderna que se adapta perfectamente a móviles y computadoras. Incluye un menú lateral (sidebar) fluido y un encabezado dinámico.Gestión de Agenda: Visualización y control de las citas médicas programadas. Permite tener una vista clara de la disponibilidad y los pacientes agendados.Entrenamiento de la Recepcionista IA (Flujos): Un panel donde puedes \"educar\" a tu asistente virtual. Aquí defines su personalidad, horarios, precios y conocimientos específicos de tu clínica.Conexión WhatsApp Web: Un módulo dedicado para vincular la cuenta oficial de la clínica, mostrando el estado de la conexión en tiempo real.Gestión de Perfil y Plan: Control de los datos del usuario, visualización del plan actual (Gratis/Premium) y límites de mensajes.Panel Administrativo: Función exclusiva para el administrador principal para gestionar métricas globales.2. La Inteligencia Artificial (IA)MediFlex utiliza el motor Gemini 1.5 Flash (o modelos superiores según configuración) para interactuar con los pacientes.Identidad Personalizable: No es un bot genérico. Mediante el System Prompt que configuras, la IA asume el rol de \"Recepcionista de la Clínica X\", adoptando el tono y la información que tú le proporciones.Reactividad Inteligente: Cuando un paciente escribe por WhatsApp, la IA analiza el mensaje, consulta sus instrucciones de entrenamiento y responde de forma natural, sin usar árboles de decisión rígidos.Automatización de Citas: Está capacitada para entender intenciones de reserva, informar sobre especialidades y filtrar consultas básicas, liberando de carga de trabajo al personal humano.3. ¿Cómo se conecta a WhatsApp Web?Técnicamente, MediFlex utiliza una librería llamada Baileys (@whiskeysockets/baileys), que es una implementación de la API multi-dispositivo de WhatsApp. Así es el proceso:Instancia de Servidor: Cuando entras a la sección de \"Configuración\", el servidor inicia un proceso de autenticación.Generación de QR: El servidor solicita un código QR a los servidores de WhatsApp. Este código se envía a tu pantalla en la WebApp.Escaneo Seguro: Al escanear el QR desde tu celular (Configuración > Dispositivos vinculados), se establece un \"túnel\" de comunicación cifrada.Sesión Persistente: Una vez conectado, el servidor guarda los datos de la sesión de forma segura. Esto permite que, aunque cierres la pestaña de la WebApp, tu recepcionista IA siga respondiendo mensajes en la nube.Escucha de Mensajes: El servidor queda \"escuchando\" los eventos de mensajes nuevos. Cada vez que llega un chat, lo procesa, le pregunta a la IA qué responder y envía la respuesta de vuelta al paciente automáticamente.En resumen: Es como tener una instancia de WhatsApp Web ejecutándose permanentemente en un servidor privado, pero potenciada con el \"cerebro\" de Google Gemini para atender a tus pacientes las 24 horas.""")
  msg2_text1 = types.Part.from_text(text="""**Developing MediFlex Concepts**

I'm currently analyzing the core functionalities described for the MediFlex WebApp. My focus is on understanding how the responsive dashboard, agenda management, and AI training features interact to create a cohesive user experience.

**Exploring MediFlex Functionality**

I'm currently processing the details of the MediFlex WebApp. My focus is on how the responsive dashboard, agenda, and AI training features integrate for an optimal user experience.

**Comprendiendo MediFlex**

I've absorbed the details of the MediFlex WebApp. My current focus is on understanding how the responsive dashboard, agenda, and AI training features synergize, particularly how the Gemini AI and WhatsApp integration function together for seamless clinic management.

**Analizando la Integración de IA**

I'm diving deeper into the MediFlex WebApp's AI capabilities. My focus is on how Gemini 1.5 Flash is leveraged for smart, personalized receptionist functions and how this integrates with the agenda and WhatsApp communication flow for enhanced patient interaction.

**Desarrollando la Arquitectura**

I'm now dissecting the proposed architecture for MediFlex. My focus is on the interplay between the frontend dashboard, the Gemini AI core, and the specific WhatsApp integration mechanisms, particularly the `Baileys` library implementation.

**Evaluando Flujos de Trabajo**

I am evaluating the described workflows within the MediFlex WebApp. My focus is on how the responsive dashboard facilitates user interaction with the AI-driven agenda management and the WhatsApp communication channels, ensuring a cohesive experience.

**Refinando la Experiencia de Usuario**

I'm now focusing on how the user interacts with the AI receptionist, specifically how Gemini's capabilities translate into intuitive conversational flows via WhatsApp, ensuring the AI's responses feel natural and efficient.

**Comprendiendo el Concepto**

I've processed the provided details regarding the MediFlex WebApp. My current focus is on the synergistic interplay between its responsive dashboard, AI-driven agenda management, and the specific WhatsApp integration using the `Baileys` library for smart receptionist functions, all powered by Gemini 1.5 Flash.""")
  msg2_text2 = types.Part.from_text(text="""Has compartido una descripción excelente y muy bien estructurada de **MediFlex**. Por lo que leo, es una plataforma robusta, moderna y altamente funcional que combina gestión administrativa tradicional con lo último en automatización mediante Inteligencia Artificial (Gemini 1.5 Flash) y WhatsApp (`Baileys`).

Como no has incluido una pregunta o instrucción específica al final de tu mensaje, entiendo que me estás dando el contexto de tu proyecto. 

¿En qué te gustaría que te ayude a continuación con MediFlex? Aquí tienes algunas ideas de lo que podemos hacer:

1. **Desarrollo del Backend (Node.js):** ¿Quieres que escriba el código base para la integración con `@whiskeysockets/baileys` (generación del QR, guardado de sesiones o la escucha de mensajes)?
2. **Integración con Gemini 1.5 Flash:** ¿Necesitas ayuda creando el código para enviar los mensajes a la API de Google, o diseñando el *System Prompt* ideal (las instrucciones maestras) para que la IA actúe como una recepcionista perfecta?
3. **Desarrollo del Frontend (React, Vue, HTML/CSS):** ¿Te gustaría crear el diseño del Panel de Control, el menú lateral fluido o la interfaz para entrenar a la IA?
4. **Base de Datos y Agenda:** ¿Buscamos la mejor manera de modelar la base de datos (ej. MongoDB o PostgreSQL) para guardar las citas, los límites de mensajes del plan o la configuración de la clínica?
5. **Redacción y Documentación:** ¿Quieres que mejore este texto para presentarlo a clientes (pitch de ventas), o que creemos un manual de usuario paso a paso?

Dime en qué área del proyecto quieres enfocarte y nos ponemos a trabajar en ello.""")
  msg4_text1 = types.Part.from_text(text="""**Developing Core Components**

I'm currently focused on architecting the fundamental frontend elements, ensuring a robust and responsive user experience. This involves defining the core components that will form the backbone of the MediFlex application.

**Integrating WhatsApp and AI**

My current focus is on seamlessly integrating the WhatsApp API with the AI model. This involves establishing secure connections and designing the logic for message processing and AI response generation.

**Establishing Backend Foundation**

I'm now focusing on setting up the backend architecture. This involves defining the database models for users, appointments, and AI configurations, and initiating the connection to MongoDB to ensure data persistence.

**Connecting WhatsApp and AI**

My current focus is on establishing a seamless link between the WhatsApp API and the AI model. This involves setting up secure communication channels and designing the message processing logic for AI response generation.

**Connecting WhatsApp and AI**

My current focus is on establishing a seamless link between the WhatsApp API and the AI model. This involves setting up secure communication channels and designing the message processing logic for AI response generation.

**Building Core Backend Functionality**

I'm currently focused on integrating the WhatsApp API and the AI model. This involves setting up the necessary services for message handling and response generation, laying the groundwork for interactive communication.""")
  msg4_text2 = types.Part.from_text(text="""Para construir **MediFlex** de forma segura, escalable y sin errores, lo mejor es dividir el proyecto en fases. Intentar programar el Frontend (la interfaz visual) y el Backend (la lógica, IA y WhatsApp) al mismo tiempo suele generar cuellos de botella.

Vamos a usar el siguiente **Stack Tecnológico**:
*   **Backend:** Node.js con Express (Rápido, ideal para WebSockets y Baileys).
*   **Base de Datos:** MongoDB (Flexible, excelente para guardar las conversaciones, configuraciones y la agenda).
*   **IA:** `@google/generative-ai` (API oficial de Gemini).
*   **WhatsApp:** `@whiskeysockets/baileys`.
*   **Frontend:** React (usando Vite) con Tailwind CSS para el diseño responsive.

Empezaremos por el **Motor Principal (Backend)**: La conexión a WhatsApp y la Inteligencia Artificial.

---

### Fase 1: Inicialización y Modelos de Base de Datos

Primero, creamos la estructura del proyecto backend e instalamos dependencias.
*(En tu terminal)*:
```bash
mkdir mediflex-backend && cd mediflex-backend
npm init -y
npm install express mongoose dotenv cors @whiskeysockets/baileys @google/generative-ai qrcode
```

Creamos el modelo de nuestra base de datos para la clínica usando **Mongoose**. Este modelo guardará la configuración del usuario y las instrucciones para la IA.

**Archivo: `src/models/Clinic.js`**
```javascript
const mongoose = require('mongoose');

const clinicSchema = new mongoose.Schema({
  name: { type: String, required: true },
  phone: { type: String, required: true }, // Número de WhatsApp conectado
  plan: { type: String, enum: ['Gratis', 'Premium'], default: 'Gratis' },
  aiSettings: {
    systemPrompt: { 
      type: String, 
      default: \"Eres el asistente virtual de MediFlex. Eres amable, profesional y ayudas a agendar citas.\" 
    },
    isActive: { type: Boolean, default: true } // Para apagar/prender la IA
  }
});

module.exports = mongoose.model('Clinic', clinicSchema);
```

---

### Fase 2: Servicio de Inteligencia Artificial (Gemini)

Vamos a crear el módulo que se encargará de recibir el mensaje del paciente, leer el *System Prompt* de la clínica, y generar la respuesta.

**Archivo: `src/services/ai.service.js`**
```javascript
const { GoogleGenerativeAI } = require(\"@google/generative-ai\");
require('dotenv').config();

// Inicializamos la API de Google con tu API Key
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

async function generateAIResponse(patientMessage, systemPrompt) {
    try {
        // Usamos Gemini 1.5 Flash como indicaste
        const model = genAI.getGenerativeModel({ model: \"gemini-1.5-flash\" });

        // Construimos el contexto (Prompt del sistema + Mensaje del paciente)
        const prompt = `
        INSTRUCCIONES DEL SISTEMA: ${systemPrompt}
        
        MENSAJE DEL PACIENTE: \"${patientMessage}\"
        
        Responde al paciente de forma natural, siguiendo estrictamente las instrucciones del sistema.
        `;

        const result = await model.generateContent(prompt);
        const response = await result.response;
        return response.text();
        
    } catch (error) {
        console.error(\"Error en Gemini IA:\", error);
        return \"Lo siento, en este momento estoy experimentando problemas técnicos. Por favor, intenta de nuevo en unos minutos.\";
    }
}

module.exports = { generateAIResponse };
```

---

### Fase 3: El \"Corazón\" - Conexión WhatsApp (Baileys)

Este es el archivo más crítico. Manejará la generación del código QR para la WebApp, guardará la sesión y escuchará los mensajes entrantes para enviarlos a la IA.

**Archivo: `src/services/whatsapp.service.js`**
```javascript
const { makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const { generateAIResponse } = require('./ai.service.js');
const Clinic = require('../models/Clinic.js'); // Para traer la configuración

// Variable global para almacenar el QR y enviarlo al Frontend
let currentQR = \"\"; 
let isConnected = false;

async function connectToWhatsApp() {
    // Guarda la sesión en la carpeta 'auth_info_baileys' para que no pida QR al reiniciar
    const { state, saveCreds } = await useMultiFileAuthState('auth_info_baileys');

    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: true, // Lo imprime en terminal (útil para pruebas)
        browser: [\"MediFlex AI\", \"Chrome\", \"1.0\"] // Nombre que sale en el celular del doctor
    });

    sock.ev.on('creds.update', saveCreds);

    // 1. GESTIÓN DE CONEXIÓN Y CÓDIGO QR
    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect, qr } = update;
        
        if (qr) {
            currentQR = qr; // Guardamos el QR para mandarlo a la WebApp
            console.log(\"QR Generado. Escanéalo desde la WebApp.\");
        }

        if (connection === 'close') {
            isConnected = false;
            const shouldReconnect = (lastDisconnect.error)?.output?.statusCode !== DisconnectReason.loggedOut;
            console.log('Conexión cerrada. ¿Reconectar?:', shouldReconnect);
            if (shouldReconnect) {
                connectToWhatsApp();
            }
        } else if (connection === 'open') {
            isConnected = true;
            currentQR = \"\"; // Limpiamos el QR porque ya se conectó
            console.log('¡WhatsApp Conectado Exitosamente a MediFlex!');
        }
    });

    // 2. ESCUCHA DE MENSAJES ENTRANTES
    sock.ev.on('messages.upsert', async (m) => {
        const msg = m.messages[0];
        // Ignorar mensajes enviados por nosotros mismos o de grupos
        if (!msg.message || msg.key.fromMe || msg.key.remoteJid.includes('@g.us')) return;

        const senderId = msg.key.remoteJid;
        // Extraer el texto del mensaje (soporta texto simple y respuestas a otros mensajes)
        const incomingText = msg.message.conversation || msg.message.extendedTextMessage?.text;

        if (incomingText) {
            console.log(`Mensaje de ${senderId}: ${incomingText}`);

            try {
                // AQUÍ OCURRE LA MAGIA: 
                // 1. Buscamos la configuración de la clínica en la BD (ej. clínica ID: 1)
                const clinicConfig = await Clinic.findOne(); 
                
                if (clinicConfig && clinicConfig.aiSettings.isActive) {
                    // 2. Enviamos el mensaje a Gemini
                    const aiReply = await generateAIResponse(incomingText, clinicConfig.aiSettings.systemPrompt);
                    
                    // 3. Respondemos por WhatsApp al paciente
                    await sock.sendMessage(senderId, { text: aiReply });
                }
            } catch (error) {
                console.error(\"Error procesando el mensaje:\", error);
            }
        }
    });

    return sock;
}

// Funciones para que el backend (Express) pueda consultar el estado
const getQR = () => currentQR;
const getConnectionStatus = () => isConnected;

module.exports = { connectToWhatsApp, getQR, getConnectionStatus };
```

---

### Fase 4: Servidor Central (Express)

Ahora unimos todo en un servidor HTTP que permitirá a la **WebApp** (Frontend) pedir el QR, ver el estado de conexión y guardar la configuración de la clínica.

**Archivo: `src/server.js`**
```javascript
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const qrcode = require('qrcode');
require('dotenv').config();

const { connectToWhatsApp, getQR, getConnectionStatus } = require('./services/whatsapp.service');
const Clinic = require('./models/Clinic');

const app = express();
app.use(cors());
app.use(express.json());

// --- RUTAS PARA WHATSAPP WEB --- //
app.get('/api/whatsapp/status', async (req, res) => {
    const isConnected = getConnectionStatus();
    if (isConnected) {
        return res.json({ status: 'connected' });
    }
    
    const qrString = getQR();
    if (qrString) {
        // Convertimos el string a una imagen Base64 para mostrarla en React
        const qrImage = await qrcode.toDataURL(qrString);
        return res.json({ status: 'qr_ready', qr: qrImage });
    }

    res.json({ status: 'starting' });
});

// --- RUTAS PARA ENTRENAMIENTO DE IA --- //
app.post('/api/clinic/prompt', async (req, res) => {
    const { systemPrompt } = req.body;
    // Buscamos o creamos la clínica
    let clinic = await Clinic.findOne();
    if (!clinic) clinic = new Clinic({ name: \"Mi Clínica\", phone: \"123456789\" });
    
    clinic.aiSettings.systemPrompt = systemPrompt;
    await clinic.save();
    
    res.json({ success: true, message: \"IA entrenada exitosamente\" });
});

// Inicialización del servidor y BD
const PORT = process.env.PORT || 3000;

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
        console.log(\"Conectado a MongoDB\");
        // Arrancamos el servicio de WhatsApp
        connectToWhatsApp();
        app.listen(PORT, () => console.log(`Servidor MediFlex corriendo en puerto ${PORT}`));
    })
    .catch(err => console.error(\"Error conectando a BD:\", err));
```

### Resumen de lo que hemos construido hasta ahora:
1. **Base de datos:** Preparada para guardar el comportamiento de la IA y si el bot está encendido/apagado.
2. **Conexión Baileys:** El servidor genera el QR. Si lo escaneas, guarda la sesión. Se queda \"escuchando\" permanentemente.
3. **Cerebro (Gemini):** Cada vez que llega un WhatsApp, el código extrae el mensaje, lo junta con el entrenamiento de tu clínica, se lo envía a Google y devuelve la respuesta al paciente de forma automática.
4. **API:** Lista para que tu Panel de Control visual (React) interactúe con el backend.

### Siguiente paso:
¿Quieres que pasemos a **crear el Frontend en React (El panel administrativo)** donde diseñaremos el Menú Lateral, el escáner del QR y la pantalla para escribir el \"System Prompt\" de la clínica? ¿O prefieres agregar el módulo de la **Agenda de Citas** en el backend primero?""")
  msg6_text1 = types.Part.from_text(text="""**Developing Core Functionality**

I'm currently focusing on integrating the Baileys library to manage WhatsApp communication and the Gemini API for advanced text generation. The backend is set up with Node.js, Express, and MongoDB, establishing a solid foundation for our operations.

**Building Appointment Logic**

I'm now shifting focus to the core functionality of MediFlex: appointment management. My immediate task is to develop the database models and backend endpoints for scheduling, allowing the AI to check availability and book appointments, which is crucial for the system's primary purpose.

**Integrating Appointment Management**

I've prioritized building the appointment scheduling backend functionality. This involves defining Mongoose models for appointments and establishing Express endpoints for creating and retrieving them. My next step is to connect this logic to the AI, enabling it to check availability and book appointments, which is a core requirement for MediFlex.

**Developing Appointment Logic**

I've prioritized building the appointment scheduling backend. This involves defining Mongoose models for appointments and establishing Express endpoints for creating and retrieving them. My next step is to connect this logic to the AI, enabling it to check availability and book appointments, a core requirement for MediFlex.

**Developing Appointment Logic**

I am now focusing on building out the core appointment scheduling functionality within the backend. This involves defining the Mongoose models for storing appointment data and creating the necessary Express endpoints for managing them. My next crucial step is to integrate this with the AI, allowing it to intelligently check availability and book appointments.""")
  msg6_text2 = types.Part.from_text(text="""Lo más lógico y profesional en este punto es **terminar la lógica del Backend agregando el módulo de Agenda de Citas**. 

¿Por qué? Porque la principal función de tu Recepcionista IA es \"Automatización de Citas\". Si construimos el Frontend ahora, la IA solo podría charlar, pero no podría agendar ni saber qué horarios están disponibles. Es mejor tener todo el \"cerebro y las bases de datos\" listos antes de pintar la interfaz visual.

Vamos a crear el sistema de Agenda y a **conectar la IA con la base de datos** para que no agende citas donde ya hay un paciente.

---

### Fase 5: Modelo de Base de Datos para la Agenda

Vamos a crear una estructura para guardar las citas médicas.

**Archivo: `src/models/Appointment.js`**
```javascript
const mongoose = require('mongoose');

const appointmentSchema = new mongoose.Schema({
  patientName: { type: String, required: false },
  patientPhone: { type: String, required: true }, // WhatsApp del paciente
  date: { type: String, required: true }, // Formato: YYYY-MM-DD
  time: { type: String, required: true }, // Formato: HH:MM
  status: { type: String, enum: ['Agendada', 'Completada', 'Cancelada'], default: 'Agendada' }
}, { timestamps: true });

module.exports = mongoose.model('Appointment', appointmentSchema);
```

---

### Fase 6: Rutas para el Panel de Control (CRUD de Agenda)

Necesitamos que el administrador (tú o los médicos) puedan ver, crear y cancelar citas desde la WebApp. Actualizamos nuestro servidor.

**Añadir en `src/server.js` (debajo de las rutas de la IA):**
```javascript
const Appointment = require('./models/Appointment');

// Obtener todas las citas (Para tu Panel de Control)
app.get('/api/appointments', async (req, res) => {
    try {
        const appointments = await Appointment.find().sort({ date: 1, time: 1 });
        res.json(appointments);
    } catch (error) {
        res.status(500).json({ error: \"Error al obtener la agenda\" });
    }
});

// Cancelar o modificar una cita manualmente
app.put('/api/appointments/:id/status', async (req, res) => {
    try {
        const { status } = req.body;
        const updated = await Appointment.findByIdAndUpdate(req.params.id, { status }, { new: true });
        res.json(updated);
    } catch (error) {
        res.status(500).json({ error: \"Error al actualizar la cita\" });
    }
});
```

---

### Fase 7: La Magia Real - Conectar Gemini con la Agenda

Aquí es donde **MediFlex** se vuelve una plataforma verdaderamente inteligente. Vamos a modificar nuestro servicio de IA para que, antes de responderle al paciente, lea la base de datos, vea qué horas están ocupadas y actúe en consecuencia.

**Actualizamos el archivo: `src/services/ai.service.js`**
```javascript
const { GoogleGenerativeAI } = require(\"@google/generative-ai\");
const Appointment = require('../models/Appointment'); // Importamos el modelo de citas
require('dotenv').config();

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

// Función auxiliar para obtener la fecha actual en formato YYYY-MM-DD
const getTodayDate = () => new Date().toISOString().split('T')[0];

async function generateAIResponse(patientMessage, patientPhone, systemPrompt) {
    try {
        const model = genAI.getGenerativeModel({ model: \"gemini-1.5-flash\" });

        // 1. Buscamos las citas que ya están agendadas desde hoy en adelante
        const today = getTodayDate();
        const futureAppointments = await Appointment.find({ 
            date: { $gte: today }, 
            status: 'Agendada' 
        });

        // 2. Creamos una lista de horarios ocupados para decírselo a la IA
        const busySlots = futureAppointments.map(app => `Fecha: ${app.date} - Hora: ${app.time}`).join('\
');

        // 3. Super-Prompt: Le inyectamos la realidad a la IA
        const contextualPrompt = `
        INSTRUCCIONES DEL SISTEMA: 
        ${systemPrompt}
        
        INFORMACIÓN EN TIEMPO REAL (ESTRICTAMENTE CONFIDENCIAL):
        - Hoy es: ${today}
        - Horarios ya ocupados en la clínica (NO PUEDES OFRECER ESTOS HORARIOS):
        ${busySlots || \"No hay citas agendadas, toda la agenda está libre.\"}
        - El número de WhatsApp del paciente con el que hablas es: ${patientPhone}

        REGLAS:
        1. Si el paciente quiere agendar y elige un horario libre, respóndele confirmando la cita y dile exactamente: \"CITA_CONFIRMADA_||[Fecha YYYY-MM-DD]||[Hora HH:MM]\".
        2. Nunca ofrezcas ni confirmes una cita en los horarios ocupados listados arriba.
        
        MENSAJE DEL PACIENTE: \"${patientMessage}\"
        `;

        const result = await model.generateContent(contextualPrompt);
        const responseText = result.response.text();
        return responseText;
        
    } catch (error) {
        console.error(\"Error en Gemini IA:\", error);
        return \"Lo siento, mi sistema de agenda está en mantenimiento un momento.\";
    }
}

module.exports = { generateAIResponse };
```

---

### Fase 8: Automatizar la creación de la cita en WhatsApp

Ahora, si la IA decide que el horario es válido y confirma la cita, debemos \"atrapar\" esa confirmación en el código de WhatsApp y guardarla en la base de datos automáticamente.

**Actualizamos la escucha de mensajes en: `src/services/whatsapp.service.js`**
```javascript
// ... (código anterior)

            try {
                const clinicConfig = await Clinic.findOne(); 
                
                if (clinicConfig && clinicConfig.aiSettings.isActive) {
                    // Pasamos también el número de teléfono (senderId)
                    let aiReply = await generateAIResponse(incomingText, senderId, clinicConfig.aiSettings.systemPrompt);
                    
                    // INTERCEPTOR DE CITAS: Buscamos si la IA intentó confirmar una cita
                    const regexCita = /CITA_CONFIRMADA_\\|\\|(.*?)\\|\\|(.*?)(\\s|$)/;
                    const match = aiReply.match(regexCita);

                    if (match) {
                        const date = match[1]; // YYYY-MM-DD
                        const time = match[2]; // HH:MM

                        // Guardamos la cita automáticamente en MongoDB
                        const newAppointment = new Appointment({
                            patientPhone: senderId.replace('@s.whatsapp.net', ''),
                            date: date,
                            time: time
                        });
                        await newAppointment.save();

                        console.log(`¡NUEVA CITA GUARDADA! ${date} a las ${time}`);

                        // Limpiamos el mensaje de la IA para que el paciente no vea códigos extraños
                        aiReply = aiReply.replace(regexCita, `¡Tu cita ha sido agendada exitosamente para el día ${date} a las ${time}! Te esperamos.`);
                    }

                    // Respondemos por WhatsApp al paciente
                    await sock.sendMessage(senderId, { text: aiReply });
                }
            }
// ... (resto del código)
```

### ¿Qué hemos logrado con esto?
Con un ingenioso uso del *System Prompt*, hemos convertido a Gemini en un agente con conexión a tu base de datos.
1. El paciente escribe: *\"Quiero una cita el 20 de Octubre a las 10:00\"*.
2. El sistema saca las citas de MongoDB, y se las envía ocultas a la IA.
3. Si a las 10:00 está libre, la IA responde con una clave secreta (`CITA_CONFIRMADA_||2023-10-20||10:00`).
4. Tu código (Baileys) detecta esa clave, la borra para que el paciente no la vea, **guarda la cita en la base de datos** y le avisa al paciente que todo está listo.

### ¡El Backend está 100% completo! 🎉
Tenemos Bases de datos, IA inteligente que agenda, API de WhatsApp Web, y Rutas de Administrador.

**Siguiente paso natural:** Ahora sí es el momento ideal para empezar a crear el **Frontend (La WebApp en React)**.
¿Te parece si empezamos por crear el **Panel de Control (Dashboard)** con el menú lateral, o prefieres empezar por la **Pantalla de conexión de WhatsApp (donde sale el código QR)**?""")
  msg8_text1 = types.Part.from_text(text="""**Developing Backend Architecture**

I'm continuing to refine the backend architecture for MediFlex, focusing on database design and API endpoint definitions. My current thoughts are centered on establishing a robust and scalable foundation for our services.

**Initiating Frontend Framework**

I'm now commencing the frontend development phase. My immediate focus is on setting up the React project using Vite and Tailwind CSS, and then building out the core responsive dashboard layout, including the dynamic header and fluid sidebar navigation. This will provide the foundational structure for all upcoming features.

**Initializing Frontend Structure**

I've decided to proceed with setting up the core frontend structure. This involves initiating a new React project using Vite and Tailwind CSS, and then immediately building out the responsive dashboard layout with a dynamic header and fluid sidebar navigation as a foundational shell.

**Initializing Frontend Framework**

I've decided to proceed with setting up the core frontend structure. This involves initiating a new React project using Vite and Tailwind CSS, and then immediately building out the responsive dashboard layout with a dynamic header and fluid sidebar navigation as a foundational shell.""")
  msg8_text2 = types.Part.from_text(text="""¡Perfecto! Como ya tenemos un Backend robusto que hace todo el trabajo pesado, lo más inteligente ahora es construir el **esqueleto visual de nuestra WebApp (Frontend)**. 

No podemos poner los muebles si no hemos construido la casa. Así que vamos a crear la estructura base en **React**, configurar las rutas y diseñar el **Panel de Control Responsive** (con su menú lateral y encabezado) que mencionaste en tu primera descripción.

Para esto usaremos **Vite** (súper rápido), **React**, **Tailwind CSS** (para que se vea moderno y se adapte a celulares) y **Lucide React** (para los íconos).

---

### Fase 9: Inicializar el Frontend

Abre una nueva terminal (deja corriendo la del backend si la tienes encendida) y ejecuta estos comandos:

```bash
# Creamos el proyecto de React
npm create vite@latest mediflex-frontend -- --template react
cd mediflex-frontend

# Instalamos Tailwind CSS, React Router y los íconos
npm install react-router-dom lucide-react axios
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Configuramos **Tailwind**. Abre el archivo `tailwind.config.js` y asegúrate de que quede así:
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    \"./index.html\",
    \"./src/**/*.{js,ts,jsx,tsx}\",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#2563EB', // Un azul médico moderno
        secondary: '#10B981', // Verde estilo WhatsApp
      }
    },
  },
  plugins: [],
}
```

Añade las directivas de Tailwind en `src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  background-color: #f3f4f6; /* Fondo gris claro */
}
```

---

### Fase 10: El Menú Lateral (Sidebar) y el Encabezado (Header)

Vamos a crear el \"molde\" de la plataforma. Este componente envolverá todas nuestras pantallas.

Crea una carpeta `src/components` y dentro un archivo llamado `Layout.jsx`:

**Archivo: `src/components/Layout.jsx`**
```jsx
import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Home, Calendar, Bot, Smartphone, Settings, Menu, X } from 'lucide-react';

export default function Layout({ children }) {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const location = useLocation();

  const menuItems = [
    { name: 'Panel Principal', icon: Home, path: '/' },
    { name: 'Agenda', icon: Calendar, path: '/agenda' },
    { name: 'WhatsApp Web', icon: Smartphone, path: '/whatsapp' },
    { name: 'Entrenar IA', icon: Bot, path: '/ai-training' },
    { name: 'Configuración', icon: Settings, path: '/settings' },
  ];

  return (
    <div className=\"flex h-screen bg-gray-100\">
      
      {/* SIDEBAR RESPONSIVE */}
      <aside className={`bg-white text-gray-800 w-64 flex-shrink-0 shadow-lg transition-transform transform ${isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full'} md:translate-x-0 fixed md:relative z-20 h-full`}>
        <div className=\"flex items-center justify-between p-4 border-b\">
          <h1 className=\"text-2xl font-bold text-primary\">Medi<span className=\"text-secondary\">Flex</span></h1>
          <button className=\"md:hidden text-gray-500\" onClick={() => setIsMobileMenuOpen(false)}>
            <X size={24} />
          </button>
        </div>
        <nav className=\"p-4 space-y-2\">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            return (
              <Link 
                key={item.name} 
                to={item.path}
                className={`flex items-center space-x-3 p-3 rounded-lg transition-colors ${isActive ? 'bg-primary text-white' : 'hover:bg-blue-50 text-gray-600'}`}
              >
                <Icon size={20} />
                <span className=\"font-medium\">{item.name}</span>
              </Link>
            );
          })}
        </nav>
      </aside>

      {/* ÁREA PRINCIPAL */}
      <main className=\"flex-1 flex flex-col min-w-0 overflow-hidden\">
        {/* ENCABEZADO DINÁMICO */}
        <header className=\"bg-white shadow-sm h-16 flex items-center justify-between px-4 lg:px-8 z-10\">
          <button className=\"md:hidden text-gray-600\" onClick={() => setIsMobileMenuOpen(true)}>
            <Menu size={24} />
          </button>
          
          <div className=\"flex-1 md:flex-none\"></div>

          {/* Gestión de Perfil y Plan */}
          <div className=\"flex items-center space-x-4\">
            <div className=\"text-right hidden sm:block\">
              <p className=\"text-sm font-bold text-gray-800\">Clínica Central</p>
              <p className=\"text-xs text-secondary font-semibold\">Plan Premium</p>
            </div>
            <div className=\"h-10 w-10 bg-primary text-white rounded-full flex items-center justify-center font-bold text-lg\">
              C
            </div>
          </div>
        </header>

        {/* CONTENIDO DE LAS PANTALLAS */}
        <div className=\"flex-1 overflow-auto p-4 lg:p-8\">
          {children}
        </div>
      </main>

      {/* Overlay para móviles */}
      {isMobileMenuOpen && (
        <div 
          className=\"fixed inset-0 bg-black bg-opacity-50 z-10 md:hidden\"
          onClick={() => setIsMobileMenuOpen(false)}
        ></div>
      )}
    </div>
  );
}
```

---

### Fase 11: Configurar las Rutas y las Pantallas \"Dummy\"

Ahora, le decimos a React que use este Layout y creamos los espacios para nuestras futuras pantallas.

Edita el archivo `src/App.jsx`:

**Archivo: `src/App.jsx`**
```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';

// Componentes temporales (Los iremos construyendo de verdad después)
const Dashboard = () => <h2 className=\"text-2xl font-bold\">Métricas y Resumen Global 📊</h2>;
const Agenda = () => <h2 className=\"text-2xl font-bold\">Gestión de Agenda de Citas 📅</h2>;
const WhatsAppConfig = () => <h2 className=\"text-2xl font-bold\">Conexión a WhatsApp Web 📱</h2>;
const AITraining = () => <h2 className=\"text-2xl font-bold\">Entrenamiento de la Recepcionista IA 🧠</h2>;

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path=\"/\" element={<Dashboard />} />
          <Route path=\"/agenda\" element={<Agenda />} />
          <Route path=\"/whatsapp\" element={<WhatsAppConfig />} />
          <Route path=\"/ai-training\" element={<AITraining />} />
          <Route path=\"/settings\" element={<h2 className=\"text-2xl font-bold\">Configuración de la Clínica ⚙️</h2>} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
```

---

### ¡Estructura de la WebApp terminada!

Si ejecutas `npm run dev` en la consola de tu frontend, verás una interfaz muy profesional. 
* Tienes un Menú Lateral que resalta en qué sección estás.
* En móviles, el menú se oculta y aparece con un botón de hamburguesa.
* Tienes tu indicador de \"Plan Premium\" en la esquina superior derecha.

**El siguiente paso natural es dar vida a una de estas pantallas \"vacías\" conectándolas a nuestro Backend.**

Dado que el corazón del proyecto es la automatización, ¿Qué pantalla te gustaría que programemos primero?
1. **La Pantalla de WhatsApp (`/whatsapp`):** Donde mostraremos el Código QR para que vincules el teléfono y veremos el estado de la conexión en vivo.
2. **La Pantalla de Entrenamiento IA (`/ai-training`):** El panel de control donde escribes el *System Prompt* y le das a guardar para modificar la personalidad de la recepcionista.
3. **La Pantalla de Agenda (`/agenda`):** Donde consultaremos la base de datos para mostrar un listado/calendario visual de los pacientes agendados. 

¿Cuál prefieres atacar primero?""")
  msg10_text1 = types.Part.from_text(text="""**Refining User Experience**

I'm now focusing on enhancing the user experience for the MediFlex app, prioritizing intuitive navigation and clear feedback mechanisms to ensure a smooth interaction for all users.

**Connecting WhatsApp Service**

My immediate focus is on implementing the WhatsApp connection screen. This is the critical first step, as it enables the core functionality of receiving messages and facilitating AI-driven appointment bookings through the Baileys integration.

**Connecting WhatsApp Service**

My immediate focus is on implementing the WhatsApp connection screen. This is the critical first step, as it enables the core functionality of receiving messages and facilitating AI-driven appointment bookings through the Baileys integration.

**Establishing WhatsApp Connectivity**

I am now focused on implementing the critical WhatsApp connection screen. This step is paramount to enabling the core functionality of receiving patient messages and initiating AI-driven appointment bookings via the Baileys integration.

**Connecting WhatsApp Gateway**

I'm now prioritizing the integration of the WhatsApp connection screen. This is a pivotal step, allowing the app to receive incoming patient messages and kickstart the AI-powered appointment booking process through the Baileys integration.""")
  msg10_text2 = types.Part.from_text(text="""Para garantizar que el sistema funcione sin errores y de forma lógica, **el paso más crítico ahora es construir la Pantalla de Conexión a WhatsApp**. 

¿Por qué? Porque WhatsApp es el \"puente\" de nuestra clínica. Si no vinculamos el teléfono, la Inteligencia Artificial no podrá recibir mensajes ni agendar citas, y las demás pantallas no tendrían datos reales con los que trabajar.

Vamos a crear una pantalla inteligente que se comunique con el Backend, solicite el código QR y, una vez que lo escanees con tu celular, actualice la pantalla automáticamente mostrando que estás conectado.

---

### Fase 12: Creación de la Pantalla de WhatsApp Web

Primero, vamos a organizar nuestras pantallas. Crea una carpeta llamada `src/pages` y dentro crea el archivo `WhatsAppConfig.jsx`.

Esta pantalla hará \"polling\" (preguntarle al servidor cada 3 segundos) para saber si hay un QR nuevo o si ya te conectaste.

**Archivo: `src/pages/WhatsAppConfig.jsx`**
```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Smartphone, CheckCircle, RefreshCw, AlertTriangle } from 'lucide-react';

export default function WhatsAppConfig() {
  const [status, setStatus] = useState('starting'); // 'starting', 'qr_ready', 'connected', 'error'
  const [qrCode, setQrCode] = useState('');
  
  // URL de tu backend (Asegúrate de que el backend esté corriendo en el puerto 3000)
  const API_URL = 'http://localhost:3000/api/whatsapp/status';

  const checkWhatsAppStatus = async () => {
    try {
      const response = await axios.get(API_URL);
      setStatus(response.data.status);
      
      if (response.data.status === 'qr_ready') {
        setQrCode(response.data.qr);
      }
    } catch (error) {
      console.error(\"Error conectando al backend:\", error);
      setStatus('error');
    }
  };

  useEffect(() => {
    // Revisamos el estado inmediatamente al entrar a la pantalla
    checkWhatsAppStatus();

    // Configuramos un temporizador para revisar el estado cada 3 segundos
    // Esto permite que si escaneas el QR, la pantalla cambie sola a \"Conectado\"
    const interval = setInterval(() => {
      checkWhatsAppStatus();
    }, 3000);

    // Limpiamos el temporizador si el usuario cambia a otra pantalla para evitar errores
    return () => clearInterval(interval);
  }, []);

  return (
    <div className=\"max-w-3xl mx-auto\">
      <div className=\"mb-8\">
        <h2 className=\"text-3xl font-bold text-gray-800\">Conexión de WhatsApp</h2>
        <p className=\"text-gray-600 mt-2\">
          Vincula el número de tu clínica para que la Recepcionista IA comience a atender pacientes.
        </p>
      </div>

      <div className=\"bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden\">
        <div className=\"p-6 md:p-10 flex flex-col items-center justify-center text-center\">
          
          {/* ESTADO: CARGANDO / INICIANDO */}
          {status === 'starting' && (
            <div className=\"flex flex-col items-center py-10\">
              <RefreshCw className=\"w-16 h-16 text-primary animate-spin mb-4\" />
              <h3 className=\"text-xl font-semibold\">Iniciando el servidor de WhatsApp...</h3>
              <p className=\"text-gray-500 mt-2\">Por favor, espera unos segundos.</p>
            </div>
          )}

          {/* ESTADO: QR LISTO PARA ESCANEAR */}
          {status === 'qr_ready' && (
            <div className=\"flex flex-col items-center\">
              <div className=\"bg-blue-50 text-primary px-4 py-2 rounded-full font-medium mb-6 flex items-center\">
                <Smartphone className=\"w-5 h-5 mr-2\" />
                Esperando vinculación
              </div>
              
              <div className=\"p-4 bg-white border-4 border-gray-100 rounded-2xl shadow-sm mb-6\">
                {qrCode ? (
                  <img src={qrCode} alt=\"Código QR de WhatsApp\" className=\"w-64 h-64\" />
                ) : (
                  <div className=\"w-64 h-64 bg-gray-100 flex items-center justify-center animate-pulse rounded-xl\">
                    Cargando QR...
                  </div>
                )}
              </div>

              <h3 className=\"text-xl font-bold text-gray-800 mb-2\">Escanea el código QR</h3>
              <ol className=\"text-left text-gray-600 space-y-2 max-w-sm mt-4\">
                <li>1. Abre WhatsApp en tu teléfono.</li>
                <li>2. Toca Menú o Configuración y selecciona <strong>Dispositivos vinculados</strong>.</li>
                <li>3. Toca <strong>Vincular un dispositivo</strong>.</li>
                <li>4. Apunta tu teléfono a esta pantalla para escanear el código.</li>
              </ol>
            </div>
          )}

          {/* ESTADO: CONECTADO EXITOSAMENTE */}
          {status === 'connected' && (
            <div className=\"flex flex-col items-center py-10\">
              <div className=\"w-24 h-24 bg-green-100 rounded-full flex items-center justify-center mb-6\">
                <CheckCircle className=\"w-12 h-12 text-secondary\" />
              </div>
              <h3 className=\"text-2xl font-bold text-gray-800 mb-2\">¡WhatsApp Conectado!</h3>
              <p className=\"text-gray-600 max-w-md\">
                Tu línea está sincronizada correctamente. La Inteligencia Artificial ya está activa y escuchando los mensajes de tus pacientes en tiempo real.
              </p>
            </div>
          )}

          {/* ESTADO: ERROR DE CONEXIÓN */}
          {status === 'error' && (
            <div className=\"flex flex-col items-center py-10\">
              <AlertTriangle className=\"w-16 h-16 text-red-500 mb-4\" />
              <h3 className=\"text-xl font-semibold text-gray-800\">Error de conexión</h3>
              <p className=\"text-gray-500 mt-2 text-center max-w-md\">
                No pudimos conectar con el servidor backend. Asegúrate de que el servidor (Node.js) esté corriendo en el puerto 3000.
              </p>
            </div>
          )}
          
        </div>
      </div>
    </div>
  );
}
```

---

### Fase 13: Conectar la pantalla en el App.jsx

Ahora debemos decirle a nuestro enrutador principal que deje de mostrar el texto \"dummy\" (falso) y renderice esta nueva pantalla real que acabamos de crear.

Actualiza tu archivo **`src/App.jsx`**:

```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';

// Importamos nuestra nueva pantalla
import WhatsAppConfig from './pages/WhatsAppConfig'; 

// Componentes temporales para las demás rutas
const Dashboard = () => <h2 className=\"text-2xl font-bold\">Métricas y Resumen Global 📊</h2>;
const Agenda = () => <h2 className=\"text-2xl font-bold\">Gestión de Agenda de Citas 📅</h2>;
const AITraining = () => <h2 className=\"text-2xl font-bold\">Entrenamiento de la Recepcionista IA 🧠</h2>;

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path=\"/\" element={<Dashboard />} />
          <Route path=\"/agenda\" element={<Agenda />} />
          
          {/* Aquí inyectamos el componente real */}
          <Route path=\"/whatsapp\" element={<WhatsAppConfig />} />
          
          <Route path=\"/ai-training\" element={<AITraining />} />
          <Route path=\"/settings\" element={<h2 className=\"text-2xl font-bold\">Configuración de la Clínica ⚙️</h2>} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
```

---

### ¿Qué hace que este código prevenga errores?
1. **Manejo de estados (Status):** Si el backend tarda en generar el QR (que es normal porque depende de los servidores de Meta/WhatsApp), la pantalla muestra un estado `\"starting\"` de carga amigable, evitando que la app parezca congelada.
2. **Auto-actualización (Polling):** Al usar `setInterval`, la pantalla le pregunta sola al backend *\"¿Ya se conectó?\"*. Así, cuando escaneas el QR con tu teléfono, la pantalla en tu computadora se pone verde automáticamente (`\"connected\"`) sin que tengas que recargar la página.
3. **Limpieza de memoria (Cleanup):** Al usar `clearInterval`, evitamos fugas de memoria (memory leaks) si el usuario decide hacer clic en otra pestaña del menú antes de escanear el QR.

### El Siguiente Paso Lógico

Ahora que nuestra clínica puede \"escuchar\" a través de WhatsApp, **necesitamos enseñarle cómo debe hablar y qué servicios ofrece la clínica.**

Lo más inteligente ahora es construir la **Pantalla de Entrenamiento de la IA (`/ai-training`)**, donde crearemos un formulario para redactar el *System Prompt* y guardarlo en la Base de Datos. ¿Procedo a construir esta pantalla?""")
  msg12_text1 = types.Part.from_text(text="""**Configuring AI Training Screen**

I'm focusing on implementing the AI Training Screen functionality. My current efforts involve enabling clinic administrators to define the AI's persona, rules, and knowledge base via the System Prompt. The next step is to ensure this configuration is reliably saved into the MongoDB database.

**Designing AI Training Form**

I'm designing the AI training form. I’ll create a new React component, including a textarea for the system prompt and an activation toggle. Next, I’ll fetch existing settings upon page load and connect the form to the backend.

**Implementing AI Training Page**

I'm moving forward with creating the `AITraining` page. My focus is on building the React component to manage the system prompt and activation toggle. I'll ensure it fetches existing settings and connects to the backend for saving.

**Configuring AI System Prompt**

I'm now implementing the AI configuration page. This involves creating a new React component that will allow administrators to define the AI's system prompt and an activation toggle. I'll fetch existing settings and connect this form to the backend for seamless saving.

**Building AI Training Interface**

I'm now focused on constructing the `AITraining` React page. This involves creating a form with a textarea for the system prompt and an activation toggle. I'll also implement the logic to fetch existing settings on load and save them via the backend.""")
  msg12_text2 = types.Part.from_text(text="""¡Excelente elección! Para que la Inteligencia Artificial sea útil y no un simple robot genérico, debemos darle una \"identidad\" y reglas claras (horarios, precios, especialidades).

Antes de crear la pantalla visual en React, nos dimos cuenta de un pequeño detalle técnico: en el Backend (Fase 4) creamos la ruta para **guardar** las instrucciones (`POST`), pero olvidamos crear la ruta para **leerlas** (`GET`). Si no leemos las instrucciones, cada vez que abras la pantalla de entrenamiento, el cuadro de texto aparecerá vacío.

Vamos a hacer este pequeño ajuste rápido en el Backend y luego creamos la pantalla.

---

### Fase 14.1: Ajuste rápido en el Backend (Node.js)

Ve a tu archivo **`src/server.js`** en el backend. Busca la sección `// --- RUTAS PARA ENTRENAMIENTO DE IA --- //` y **reemplázala** con esto:

```javascript
// --- RUTAS PARA CONFIGURACIÓN DE IA --- //

// 1. Obtener la configuración actual
app.get('/api/clinic/settings', async (req, res) => {
    try {
        let clinic = await Clinic.findOne();
        // Si no existe, devolvemos datos por defecto
        if (!clinic) {
            return res.json({ systemPrompt: \"\", isActive: false });
        }
        res.json(clinic.aiSettings);
    } catch (error) {
        res.status(500).json({ error: \"Error al obtener la configuración\" });
    }
});

// 2. Guardar o actualizar la configuración
app.post('/api/clinic/settings', async (req, res) => {
    try {
        const { systemPrompt, isActive } = req.body;
        
        let clinic = await Clinic.findOne();
        if (!clinic) {
            clinic = new Clinic({ name: \"Clínica Central\", phone: \"Pendiente\" });
        }
        
        clinic.aiSettings.systemPrompt = systemPrompt;
        clinic.aiSettings.isActive = isActive;
        await clinic.save();
        
        res.json({ success: true, message: \"IA entrenada exitosamente\" });
    } catch (error) {
        res.status(500).json({ error: \"Error al guardar la configuración\" });
    }
});
```
*(Guarda el archivo y reinicia tu servidor backend si no usa `nodemon`)*.

---

### Fase 14.2: Pantalla de Entrenamiento de la IA (Frontend)

Ahora sí, vamos a nuestro proyecto en React. Crea un archivo llamado `AITraining.jsx` dentro de la carpeta `src/pages`.

Esta pantalla tendrá:
1. Un interruptor (Toggle) para encender/apagar a la recepcionista.
2. Un área de texto grande para escribir las instrucciones.
3. Alertas visuales para saber si se guardó correctamente.

**Archivo: `src/pages/AITraining.jsx`**
```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bot, Save, Power, PowerOff, CheckCircle, AlertCircle } from 'lucide-react';

export default function AITraining() {
  const [systemPrompt, setSystemPrompt] = useState('');
  const [isActive, setIsActive] = useState(false);
  
  const [isLoading, setIsLoading] = useState(true);
  const [isSaving, setIsSaving] = useState(false);
  const [alert, setAlert] = useState({ show: false, type: '', message: '' });

  const API_URL = 'http://localhost:3000/api/clinic/settings';

  // 1. Cargar la configuración actual al abrir la pantalla
  useEffect(() => {
    const fetchSettings = async () => {
      try {
        const response = await axios.get(API_URL);
        setSystemPrompt(response.data.systemPrompt || '');
        setIsActive(response.data.isActive || false);
      } catch (error) {
        console.error(\"Error cargando la configuración:\", error);
      } finally {
        setIsLoading(false);
      }
    };
    fetchSettings();
  }, []);

  // 2. Guardar los cambios en el backend
  const handleSave = async () => {
    setIsSaving(true);
    setAlert({ show: false, type: '', message: '' });

    try {
      await axios.post(API_URL, { systemPrompt, isActive });
      setAlert({ 
        show: true, 
        type: 'success', 
        message: '¡Configuración guardada! La IA ya está usando estas instrucciones.' 
      });
      
      // Ocultar alerta después de 3 segundos
      setTimeout(() => setAlert({ show: false, type: '', message: '' }), 3000);
    } catch (error) {
      setAlert({ 
        show: true, 
        type: 'error', 
        message: 'Error al guardar. Verifica tu conexión.' 
      });
    } finally {
      setIsSaving(false);
    }
  };

  if (isLoading) {
    return <div className=\"p-8 text-gray-500\">Cargando cerebro de la IA...</div>;
  }

  return (
    <div className=\"max-w-4xl mx-auto\">
      <div className=\"mb-8\">
        <h2 className=\"text-3xl font-bold text-gray-800 flex items-center\">
          <Bot className=\"w-8 h-8 mr-3 text-primary\" />
          Entrenamiento de la IA
        </h2>
        <p className=\"text-gray-600 mt-2\">
          Define la personalidad, el tono y los conocimientos de tu recepcionista virtual.
        </p>
      </div>

      {/* Alerta de Éxito o Error */}
      {alert.show && (
        <div className={`p-4 rounded-lg mb-6 flex items-center ${alert.type === 'success' ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-700'}`}>
          {alert.type === 'success' ? <CheckCircle className=\"w-5 h-5 mr-2\" /> : <AlertCircle className=\"w-5 h-5 mr-2\" />}
          {alert.message}
        </div>
      )}

      <div className=\"bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden\">
        <div className=\"p-6 md:p-8\">
          
          {/* CONTROL: Encender / Apagar */}
          <div className=\"flex items-center justify-between p-4 bg-gray-50 rounded-lg mb-8 border border-gray-200\">
            <div>
              <h3 className=\"text-lg font-semibold text-gray-800\">Estado de la Recepcionista</h3>
              <p className=\"text-sm text-gray-500\">Si la apagas, no responderá mensajes en WhatsApp.</p>
            </div>
            <button 
              onClick={() => setIsActive(!isActive)}
              className={`flex items-center px-4 py-2 rounded-full font-medium transition-colors ${
                isActive ? 'bg-green-100 text-green-700 hover:bg-green-200' : 'bg-red-100 text-red-700 hover:bg-red-200'
              }`}
            >
              {isActive ? <Power className=\"w-5 h-5 mr-2\" /> : <PowerOff className=\"w-5 h-5 mr-2\" />}
              {isActive ? 'IA Activada' : 'IA Apagada'}
            </button>
          </div>

          {/* CONTROL: Instrucciones (System Prompt) */}
          <div className=\"mb-6\">
            <label className=\"block text-gray-700 font-bold mb-2 text-lg\">
              Instrucciones Maestras (System Prompt)
            </label>
            <p className=\"text-gray-500 text-sm mb-4\">
              Escribe cómo quieres que atienda. Incluye saludos, especialidades médicas, precios de consulta, dirección de la clínica y reglas de respuesta.
            </p>
            
            <textarea
              value={systemPrompt}
              onChange={(e) => setSystemPrompt(e.target.value)}
              className=\"w-full h-80 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary outline-none resize-y font-mono text-sm\"
              placeholder={`Ejemplo:
Eres Ana, la recepcionista virtual de \"Clínica Salud+\".
Tu tono debe ser muy amable, profesional y empático.
Nuestros servicios son:
- Consulta General ($40)
- Odontología ($50)
- Pediatría ($60)
Nuestra dirección es Av. Principal 123.
Si el paciente quiere agendar, pídele que te diga qué especialidad busca...`}
            ></textarea>
          </div>

          {/* BOTÓN DE GUARDADO */}
          <div className=\"flex justify-end\">
            <button
              onClick={handleSave}
              disabled={isSaving}
              className={`flex items-center px-6 py-3 bg-primary text-white font-bold rounded-lg shadow hover:bg-blue-700 transition-colors ${isSaving ? 'opacity-70 cursor-not-allowed' : ''}`}
            >
              {isSaving ? (
                <div className=\"w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin mr-2\"></div>
              ) : (
                <Save className=\"w-5 h-5 mr-2\" />
              )}
              {isSaving ? 'Guardando...' : 'Guardar Entrenamiento'}
            </button>
          </div>

        </div>
      </div>
    </div>
  );
}
```

---

### Fase 14.3: Conectar la pantalla en App.jsx

Igual que hicimos antes, debemos reemplazar la pantalla \"falsa\" por nuestra nueva pantalla interactiva.

Edita tu archivo **`src/App.jsx`**:

```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';

import WhatsAppConfig from './pages/WhatsAppConfig';
import AITraining from './pages/AITraining'; // <-- Importamos la nueva pantalla

const Dashboard = () => <h2 className=\"text-2xl font-bold\">Métricas y Resumen Global 📊</h2>;
const Agenda = () => <h2 className=\"text-2xl font-bold\">Gestión de Agenda de Citas 📅</h2>;

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path=\"/\" element={<Dashboard />} />
          <Route path=\"/agenda\" element={<Agenda />} />
          <Route path=\"/whatsapp\" element={<WhatsAppConfig />} />
          
          {/* Inyectamos el componente real */}
          <Route path=\"/ai-training\" element={<AITraining />} />
          
          <Route path=\"/settings\" element={<h2 className=\"text-2xl font-bold\">Configuración de la Clínica ⚙️</h2>} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
```

### ¿Por qué esta pantalla es el núcleo del producto?
Con este módulo, ya no tienes que modificar el código para cambiar cómo actúa la clínica. Si mañana la clínica sube el precio de sus consultas o agrega un \"Cardiólogo\", el administrador solo tiene que entrar a esta pantalla, modificar el texto, darle a **Guardar**, ¡y la IA en WhatsApp empezará a dar los precios nuevos al instante!

### El Próximo y Último Gran Reto: La Agenda 📅

Ahora que la IA puede conectarse a WhatsApp y sabe qué decir, lo único que nos falta visualmente es **La Pantalla de Agenda (`/agenda`)**.

Aquí es donde mostraremos las citas que la IA vaya confirmando (que diseñamos en el Backend en la Fase 7 y 8). Construiremos una tabla o lista donde el médico pueda ver qué pacientes están agendados y sus horarios. 

¿Quieres que proceda a construir la **Gestión de Agenda**?""")
  msg14_text1 = types.Part.from_text(text="""**Developing Agenda View**

I'm focusing on constructing the frontend for the agenda screen. My current thoughts are centered on laying out the core components and ensuring a user-friendly interface for managing tasks and events.

**Designing Agenda UI**

I'm currently mapping out the structure for the agenda view, considering how best to present appointment data. My focus is on creating an intuitive table layout with essential details, and planning for interactive elements to manage appointment statuses.

**Building Agenda Component**

I am currently focused on developing the frontend for the agenda screen, specifically `Agenda.jsx`. My efforts are directed towards fetching appointment data from the API, structuring it into a clear table format, and implementing the logic for updating appointment statuses.

**Constructing Agenda Page**

I'm now building out the `Agenda.jsx` frontend component. My focus is on fetching appointment data, displaying it in a clear table with status indicators, and implementing the functionality to update appointment statuses directly from this view, aiming for an intuitive user experience.""")
  msg14_text2 = types.Part.from_text(text="""¡Manos a la obra! Esta es una de las pantallas más gratificantes porque aquí es donde veremos el fruto del trabajo de la IA. Cada vez que Gemini confirme una cita por WhatsApp, aparecerá automáticamente en esta pantalla.

Vamos a crear una interfaz limpia donde el administrador pueda ver el listado de pacientes, la fecha, la hora, y tenga botones para cambiar el estado de la cita (por ejemplo, marcarla como \"Completada\" cuando el paciente asista, o \"Cancelada\").

---

### Fase 15.1: Creación de la Pantalla de Agenda

Crea un archivo llamado `Agenda.jsx` dentro de la carpeta `src/pages`.

**Archivo: `src/pages/Agenda.jsx`**
```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Calendar, Clock, User, Phone, CheckCircle, XCircle, RefreshCw } from 'lucide-react';

export default function Agenda() {
  const [appointments, setAppointments] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isRefreshing, setIsRefreshing] = useState(false);

  const API_URL = 'http://localhost:3000/api/appointments';

  // 1. Función para obtener las citas desde la Base de Datos
  const fetchAppointments = async () => {
    try {
      const response = await axios.get(API_URL);
      setAppointments(response.data);
    } catch (error) {
      console.error(\"Error cargando la agenda:\", error);
    } finally {
      setIsLoading(false);
      setIsRefreshing(false);
    }
  };

  // Cargar al inicio
  useEffect(() => {
    fetchAppointments();
  }, []);

  // 2. Función para cambiar el estado de la cita (Completar o Cancelar)
  const handleUpdateStatus = async (id, newStatus) => {
    try {
      // Actualizamos en el backend
      await axios.put(`${API_URL}/${id}/status`, { status: newStatus });
      
      // Actualizamos visualmente en el frontend sin tener que recargar toda la página
      setAppointments(prev => 
        prev.map(app => app._id === id ? { ...app, status: newStatus } : app)
      );
    } catch (error) {
      alert(\"Error al actualizar la cita.\");
    }
  };

  const handleRefresh = () => {
    setIsRefreshing(true);
    fetchAppointments();
  };

  // 3. Funciones auxiliares para colores visuales
  const getStatusBadge = (status) => {
    switch (status) {
      case 'Agendada':
        return <span className=\"px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold\">Agendada</span>;
      case 'Completada':
        return <span className=\"px-3 py-1 bg-green-100 text-green-700 rounded-full text-xs font-bold\">Completada</span>;
      case 'Cancelada':
        return <span className=\"px-3 py-1 bg-red-100 text-red-700 rounded-full text-xs font-bold\">Cancelada</span>;
      default:
        return <span>{status}</span>;
    }
  };

  if (isLoading) {
    return <div className=\"p-8 text-gray-500 flex items-center\"><RefreshCw className=\"animate-spin mr-2\" /> Cargando agenda...</div>;
  }

  return (
    <div className=\"max-w-6xl mx-auto\">
      {/* ENCABEZADO DE LA AGENDA */}
      <div className=\"flex flex-col md:flex-row md:items-center justify-between mb-8 gap-4\">
        <div>
          <h2 className=\"text-3xl font-bold text-gray-800 flex items-center\">
            <Calendar className=\"w-8 h-8 mr-3 text-primary\" />
            Agenda de Citas
          </h2>
          <p className=\"text-gray-600 mt-2\">
            Gestiona los pacientes agendados por la Inteligencia Artificial.
          </p>
        </div>
        
        <button 
          onClick={handleRefresh}
          className=\"flex items-center px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 shadow-sm transition-colors\"
        >
          <RefreshCw className={`w-5 h-5 mr-2 ${isRefreshing ? 'animate-spin text-primary' : ''}`} />
          Actualizar Agenda
        </button>
      </div>

      {/* TABLA DE CITAS */}
      <div className=\"bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden\">
        {appointments.length === 0 ? (
          <div className=\"p-10 text-center text-gray-500\">
            <Calendar className=\"w-16 h-16 mx-auto mb-4 text-gray-300\" />
            <p className=\"text-lg font-medium\">No hay citas agendadas aún.</p>
            <p className=\"text-sm mt-1\">Cuando la IA confirme citas por WhatsApp, aparecerán aquí.</p>
          </div>
        ) : (
          <div className=\"overflow-x-auto\">
            <table className=\"w-full text-left border-collapse\">
              <thead>
                <tr className=\"bg-gray-50 text-gray-600 text-sm uppercase tracking-wider border-b\">
                  <th className=\"p-4 font-semibold\">Fecha y Hora</th>
                  <th className=\"p-4 font-semibold\">Paciente (WhatsApp)</th>
                  <th className=\"p-4 font-semibold\">Estado</th>
                  <th className=\"p-4 font-semibold text-right\">Acciones</th>
                </tr>
              </thead>
              <tbody className=\"divide-y divide-gray-100\">
                {appointments.map((appointment) => (
                  <tr key={appointment._id} className=\"hover:bg-gray-50 transition-colors\">
                    
                    {/* FECHA Y HORA */}
                    <td className=\"p-4\">
                      <div className=\"flex items-center text-gray-800 font-medium mb-1\">
                        <Calendar className=\"w-4 h-4 mr-2 text-primary\" />
                        {appointment.date}
                      </div>
                      <div className=\"flex items-center text-gray-500 text-sm\">
                        <Clock className=\"w-4 h-4 mr-2\" />
                        {appointment.time} hrs
                      </div>
                    </td>

                    {/* DATOS DEL PACIENTE */}
                    <td className=\"p-4\">
                      <div className=\"flex items-center text-gray-800 font-medium mb-1\">
                        <User className=\"w-4 h-4 mr-2 text-gray-400\" />
                        {appointment.patientName || \"Paciente Nuevo\"}
                      </div>
                      <div className=\"flex items-center text-gray-500 text-sm\">
                        <Phone className=\"w-4 h-4 mr-2 text-secondary\" />
                        +{appointment.patientPhone}
                      </div>
                    </td>

                    {/* ESTADO */}
                    <td className=\"p-4\">
                      {getStatusBadge(appointment.status)}
                    </td>

                    {/* BOTONES DE ACCIÓN */}
                    <td className=\"p-4 text-right space-x-2\">
                      {appointment.status === 'Agendada' && (
                        <>
                          <button 
                            onClick={() => handleUpdateStatus(appointment._id, 'Completada')}
                            title=\"Marcar como Completada\"
                            className=\"p-2 bg-green-50 text-green-600 rounded-lg hover:bg-green-100 transition-colors\"
                          >
                            <CheckCircle className=\"w-5 h-5\" />
                          </button>
                          <button 
                            onClick={() => handleUpdateStatus(appointment._id, 'Cancelada')}
                            title=\"Cancelar Cita\"
                            className=\"p-2 bg-red-50 text-red-600 rounded-lg hover:bg-red-100 transition-colors\"
                          >
                            <XCircle className=\"w-5 h-5\" />
                          </button>
                        </>
                      )}
                      {/* Si ya está completada o cancelada, no mostramos botones de acción (o podríamos poner un botón de eliminar) */}
                    </td>

                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
```

---

### Fase 15.2: Conectar la Agenda en App.jsx

Finalmente, reemplazamos el último componente temporal clave en nuestro enrutador.

Edita tu archivo **`src/App.jsx`**:

```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';

import WhatsAppConfig from './pages/WhatsAppConfig';
import AITraining from './pages/AITraining';
import Agenda from './pages/Agenda'; // <-- Importamos la pantalla de Agenda

// Solo nos queda el Dashboard como componente temporal
const Dashboard = () => <h2 className=\"text-2xl font-bold p-8\">Métricas y Resumen Global 📊 <br/><br/> (Próximamente)</h2>;

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path=\"/\" element={<Dashboard />} />
          
          {/* Inyectamos el componente real */}
          <Route path=\"/agenda\" element={<Agenda />} />
          
          <Route path=\"/whatsapp\" element={<WhatsAppConfig />} />
          <Route path=\"/ai-training\" element={<AITraining />} />
          <Route path=\"/settings\" element={<h2 className=\"text-2xl font-bold p-8\">Configuración de la Clínica ⚙️</h2>} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
```

---

### ¿Qué hace increíble a esta pantalla?
1. **Sinergia con Gemini:** La IA rechaza citas en horarios ocupados porque el Backend lee exactamente la misma base de datos que está dibujando esta tabla. Si tú cancelas una cita aquí, la IA sabrá automáticamente que ese espacio quedó libre nuevamente.
2. **Experiencia de Usuario (UX):** Los colores (badges) permiten a la recepcionista humana o al doctor escanear rápidamente visualmente qué citas están vigentes (azul), cuáles ya pasaron (verde) y cuáles se cayeron (rojo).
3. **Flujo de Trabajo Real:** Tienes un botón para refrescar en caso de que alguien haya agendado mientras tenías la pantalla abierta, sin necesidad de recargar todo el navegador.

### 🚀 ¡Felicidades! Tenemos el MVP (Producto Mínimo Viable) 

En este punto, **MediFlex ya es completamente funcional**:
*   ✅ **Backend:** Levanta WhatsApp y gestiona Gemini.
*   ✅ **Base de Datos:** Guarda configuraciones y Citas (MongoDB).
*   ✅ **Panel lateral y Diseño Responsive:** Listo para celular y PC.
*   ✅ **Módulo de Configuración IA:** Puedes inyectar la personalidad.
*   ✅ **Módulo de WhatsApp Web:** Genera el QR y vincula tu línea.
*   ✅ **Módulo de Agenda:** Centraliza todas las citas con acciones.

Lo único que nos restaría (si lo deseas construir ahora o en un futuro) es el **Panel Principal (Dashboard `/`)**, que sería simplemente una pantalla que lea la misma base de datos pero pinte gráficos estadísticos (Ej. \"Citas de hoy\", \"Mensajes respondidos por la IA\").

¿Quieres que proceda a construir el **Dashboard (Panel Principal)** con unas métricas bonitas para coronar el proyecto, o prefieres que revisemos cómo preparar este código para **subirlo a producción (Deploy)** en un servidor real?""")
  msg16_text1 = types.Part.from_text(text="""**Building the Dashboard Interface**

I'm focusing on constructing the core UI for the MediFlex dashboard. My current efforts are directed towards translating the MVP flow into the final major component, ensuring both aesthetic appeal and practical functionality are prioritized.

**Designing the Dashboard View**

I'm now focusing on the visual structure and data representation for the main dashboard. My current thought process involves designing the key performance indicator cards and how to best present upcoming appointment data, drawing information from the available API endpoints.

**Constructing the Dashboard View**

I'm now actively building the main dashboard component, focusing on fetching and displaying key clinic metrics. My current efforts involve integrating API calls for appointment data, AI status, and WhatsApp connectivity to populate the KPI cards and upcoming appointments list.

**Implementing the Dashboard View**

I'm now integrating the fetched appointment, AI, and WhatsApp status data into the dashboard's UI. My focus is on the final implementation of the KPI cards and the upcoming appointments list, ensuring a clean and informative presentation of real-time clinic operations.""")
  msg16_text2 = types.Part.from_text(text="""¡Excelente decisión! Un **Panel Principal (Dashboard)** es la carta de presentación de la plataforma. Es lo primero que verá el administrador o el médico al entrar, por lo que debe dar un resumen rápido y claro de cómo está funcionando la clínica en ese mismo instante.

Vamos a crear un panel que lea los datos de la Agenda, la configuración de la IA y el estado de WhatsApp para calcular métricas en tiempo real (por ejemplo: \"Citas para el día de hoy\").

---

### Fase 16.1: Creación del Dashboard

Crea un archivo llamado `Dashboard.jsx` dentro de la carpeta `src/pages`.

**Archivo: `src/pages/Dashboard.jsx`**
```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  Activity, 
  Calendar as CalendarIcon, 
  Users, 
  MessageSquare, 
  Clock, 
  CheckCircle, 
  AlertTriangle 
} from 'lucide-react';

export default function Dashboard() {
  const [appointments, setAppointments] = useState([]);
  const [waStatus, setWaStatus] = useState('starting');
  const [aiActive, setAiActive] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  // URLs de nuestra API
  const API_APPOINTMENTS = 'http://localhost:3000/api/appointments';
  const API_WA_STATUS = 'http://localhost:3000/api/whatsapp/status';
  const API_AI_SETTINGS = 'http://localhost:3000/api/clinic/settings';

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        // Hacemos las 3 peticiones al mismo tiempo para que cargue más rápido
        const [appRes, waRes, aiRes] = await Promise.all([
          axios.get(API_APPOINTMENTS).catch(() => ({ data: [] })),
          axios.get(API_WA_STATUS).catch(() => ({ data: { status: 'error' } })),
          axios.get(API_AI_SETTINGS).catch(() => ({ data: { isActive: false } }))
        ]);

        setAppointments(appRes.data);
        setWaStatus(waRes.data.status);
        setAiActive(aiRes.data.isActive);
      } catch (error) {
        console.error(\"Error cargando el dashboard:\", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  // --- CÁLCULO DE MÉTRICAS ---
  const todayDate = new Date().toISOString().split('T')[0]; // Fecha YYYY-MM-DD
  
  const citasHoy = appointments.filter(app => app.date === todayDate);
  const citasPendientes = citasHoy.filter(app => app.status === 'Agendada');
  const totalPacientes = [...new Set(appointments.map(app => app.patientPhone))].length; // Pacientes únicos

  if (isLoading) {
    return (
      <div className=\"flex flex-col items-center justify-center h-64 text-gray-500\">
        <Activity className=\"w-12 h-12 animate-pulse mb-4 text-primary\" />
        <p className=\"text-lg font-medium\">Recopilando métricas de la clínica...</p>
      </div>
    );
  }

  return (
    <div className=\"max-w-7xl mx-auto\">
      
      {/* SALUDO Y FECHA */}
      <div className=\"mb-8 flex flex-col md:flex-row md:items-end justify-between gap-4\">
        <div>
          <h2 className=\"text-3xl font-bold text-gray-800\">Hola, Administrador 👋</h2>
          <p className=\"text-gray-600 mt-2\">Este es el resumen de la clínica para el día de hoy.</p>
        </div>
        <div className=\"bg-white px-4 py-2 rounded-lg border border-gray-200 shadow-sm text-gray-700 font-medium flex items-center\">
          <CalendarIcon className=\"w-5 h-5 mr-2 text-primary\" />
          {new Date().toLocaleDateString('es-ES', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
        </div>
      </div>

      {/* TARJETAS DE MÉTRICAS (KPIs) */}
      <div className=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8\">
        
        {/* Tarjeta 1: Citas de Hoy */}
        <div className=\"bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center\">
          <div className=\"w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center mr-4\">
            <CalendarIcon className=\"w-6 h-6 text-primary\" />
          </div>
          <div>
            <p className=\"text-sm font-medium text-gray-500\">Citas para Hoy</p>
            <h3 className=\"text-2xl font-bold text-gray-800\">{citasHoy.length}</h3>
          </div>
        </div>

        {/* Tarjeta 2: Pacientes Registrados */}
        <div className=\"bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center\">
          <div className=\"w-12 h-12 rounded-full bg-purple-50 flex items-center justify-center mr-4\">
            <Users className=\"w-6 h-6 text-purple-600\" />
          </div>
          <div>
            <p className=\"text-sm font-medium text-gray-500\">Pacientes en Base</p>
            <h3 className=\"text-2xl font-bold text-gray-800\">{totalPacientes}</h3>
          </div>
        </div>

        {/* Tarjeta 3: Estado del Bot */}
        <div className=\"bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center\">
          <div className={`w-12 h-12 rounded-full flex items-center justify-center mr-4 ${aiActive ? 'bg-green-50' : 'bg-red-50'}`}>
            <Activity className={`w-6 h-6 ${aiActive ? 'text-green-600' : 'text-red-600'}`} />
          </div>
          <div>
            <p className=\"text-sm font-medium text-gray-500\">Recepcionista IA</p>
            <h3 className={`text-xl font-bold ${aiActive ? 'text-green-700' : 'text-red-700'}`}>
              {aiActive ? 'Activa' : 'Apagada'}
            </h3>
          </div>
        </div>

        {/* Tarjeta 4: Conexión WhatsApp */}
        <div className=\"bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center\">
          <div className={`w-12 h-12 rounded-full flex items-center justify-center mr-4 ${waStatus === 'connected' ? 'bg-green-50' : 'bg-yellow-50'}`}>
            <MessageSquare className={`w-6 h-6 ${waStatus === 'connected' ? 'text-secondary' : 'text-yellow-600'}`} />
          </div>
          <div>
            <p className=\"text-sm font-medium text-gray-500\">WhatsApp Web</p>
            <h3 className={`text-xl font-bold ${waStatus === 'connected' ? 'text-green-700' : 'text-yellow-700'}`}>
              {waStatus === 'connected' ? 'Conectado' : 'Desconectado'}
            </h3>
          </div>
        </div>
      </div>

      {/* SECCIÓN INFERIOR: PRÓXIMAS CITAS */}
      <div className=\"bg-white rounded-xl shadow-sm border border-gray-100 p-6\">
        <div className=\"flex items-center justify-between mb-6\">
          <h3 className=\"text-xl font-bold text-gray-800\">Próximos pacientes de hoy</h3>
          <span className=\"px-3 py-1 bg-blue-50 text-blue-700 text-sm font-semibold rounded-full\">
            {citasPendientes.length} Pendientes
          </span>
        </div>

        {citasPendientes.length === 0 ? (
          <div className=\"text-center py-8 text-gray-500 bg-gray-50 rounded-lg border border-dashed border-gray-200\">
            <CheckCircle className=\"w-12 h-12 mx-auto mb-3 text-green-400\" />
            <p className=\"font-medium\">¡No hay pacientes en espera!</p>
            <p className=\"text-sm\">La agenda de hoy está libre o todas las citas ya fueron completadas.</p>
          </div>
        ) : (
          <div className=\"space-y-4\">
            {/* Solo mostramos las próximas 5 citas para no saturar el panel */}
            {citasPendientes.slice(0, 5).map(cita => (
              <div key={cita._id} className=\"flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-blue-50 transition-colors border border-gray-100\">
                <div className=\"flex items-center\">
                  <div className=\"w-10 h-10 bg-white border border-gray-200 rounded-full flex items-center justify-center mr-4 text-primary font-bold shadow-sm\">
                    {cita.time.split(':')[0]} {/* Muestra la hora del paciente */}
                  </div>
                  <div>
                    <p className=\"font-bold text-gray-800\">{cita.patientName || \"Paciente WhatsApp\"}</p>
                    <p className=\"text-sm text-gray-500 flex items-center mt-1\">
                      <Clock className=\"w-3 h-3 mr-1\" /> {cita.time} hrs
                    </p>
                  </div>
                </div>
                <div className=\"text-right\">
                  <p className=\"text-sm font-medium text-gray-600\">Teléfono</p>
                  <p className=\"text-sm font-bold text-gray-800\">+{cita.patientPhone}</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

    </div>
  );
}
```

---

### Fase 16.2: Conectar el Dashboard en App.jsx

Esta es la última pieza del rompecabezas en nuestro enrutador. 

Actualiza tu archivo **`src/App.jsx`**:

```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';

import Dashboard from './pages/Dashboard'; // <-- Importamos el Dashboard
import WhatsAppConfig from './pages/WhatsAppConfig';
import AITraining from './pages/AITraining';
import Agenda from './pages/Agenda'; 

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          {/* Ruta Principal ahora carga nuestro Dashboard real */}
          <Route path=\"/\" element={<Dashboard />} />
          <Route path=\"/agenda\" element={<Agenda />} />
          <Route path=\"/whatsapp\" element={<WhatsAppConfig />} />
          <Route path=\"/ai-training\" element={<AITraining />} />
          <Route path=\"/settings\" element={<h2 className=\"text-2xl font-bold p-8 text-gray-700\">Configuración de la Clínica ⚙️ <br/> (En desarrollo)</h2>} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
```

---

### 🌟 Resumen de lo que logramos con el Dashboard:
1. **Vista Gerencial:** En menos de 2 segundos, el administrador sabe si el bot está funcionando, si WhatsApp está conectado y cuántos pacientes llegan hoy.
2. **Consultas Inteligentes (`Promise.all`):** En lugar de hacer que la pantalla cargue la agenda, espere, cargue WhatsApp, espere, etc., hace las tres peticiones al backend simultáneamente. Esto hace que la página cargue muchísimo más rápido.
3. **Lista de Próximos Pacientes:** Un widget limpio que filtra solo los pacientes del día actual y que aún tienen estatus \"Agendada\", ideal para la pantalla de la recepción.

---

### ¡Hemos terminado el Código de la Aplicación! 🎉🏆

A nivel de desarrollo, tienes una plataforma *Full-Stack* (Frontend + Backend + IA) moderna, funcional y estructurada para prevenir errores. 

**¿Qué sigue ahora? (El paso al mundo real)**

Tu proyecto corre perfectamente en tu computadora (`localhost`). Pero para que la clínica lo pueda usar 24/7 sin que tú tengas tu computadora encendida, se necesita el **Despliegue (Deploy)**.

Las opciones comunes para este stack son:
1. **Base de Datos (MongoDB):** Subirla a *MongoDB Atlas* (Gratis).
2. **Servidor Backend (Node.js + Baileys):** Subirlo a un VPS como *DigitalOcean* o *Render* (Se requiere un entorno que soporte guardar archivos locales de la sesión de WhatsApp).
3. **Frontend (React):** Subirlo a *Vercel* o *Netlify* (Gratis y muy rápido).

¿Te gustaría que te prepare una **Guía Paso a Paso para desplegar (subir a internet)** tu proyecto MediFlex, o prefieres hacer alguna prueba/modificación adicional en el código que ya tenemos?""")
  msg17_text1 = types.Part.from_text(text="""tengo una vm de google cloud con ubuntu desktop y me conecto a ella con el cliente nomachine, tiene 16 gb de ram es una E2""")

  model = "gemini-3.1-pro-preview"
  contents = [
    types.Content(
      role="user",
      parts=[
        msg1_text1
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg2_text1,
        msg2_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""procede a construirla en el orden que creas conveniente para evitar errores""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg4_text1,
        msg4_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""haz lo que consideres mas conveniente""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg6_text1,
        msg6_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""procede con lo que te parezca mas conveniente en este caso""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg8_text1,
        msg8_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""para evitar errores de codigo, procede con lo que consideres mas conveniente en este caso""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg10_text1,
        msg10_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""Si, procede""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg12_text1,
        msg12_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""procede, te autorizo""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg14_text1,
        msg14_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""construye el panel principal""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg16_text1,
        msg16_text2
      ]
    ),
    types.Content(
      role="user",
      parts=[
        msg17_text1
      ]
    ),
  ]
  tools = [
    types.Tool(google_search=types.GoogleSearch()),
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    tools = tools,
    thinking_config=types.ThinkingConfig(
      thinking_level="HIGH",
    ),
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    if not chunk.candidates or not chunk.candidates[0].content or not chunk.candidates[0].content.parts:
        continue
    print(chunk.text, end="")

generate()