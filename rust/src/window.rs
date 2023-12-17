use iced::{executor, Application, Command, Element, Settings, Text, Window};
use iced::{executor, Application, Command, Element, Settings, Text, Window};

pub struct HelloWorld;
impl Application for HelloWorld {
    type Executor = executor::Default;
    type Message = ();
    type Flags = ();

    fn new(_flags: ()) -> (HelloWorld, Command<Self::Message>) {
        (HelloWorld, Command::none())
    }

    fn title(&self) -> String {
        String::from("Hello, world!")
    }

    fn update(&mut self, _message: Self::Message) -> Command<Self::Message> {
        Command::none()
    }

    fn view(&mut self) -> Element<Self::Message> {
        Text::new("Hello, world!").into()
    }

    type Theme = iced::Default;

    
}

pub fn windowz() {
    HelloWorld::run(Settings {
        window: Window::new()
            .title("Hello, world!")
            .size(200, 100),
        ..Settings::default()
    }); 
}