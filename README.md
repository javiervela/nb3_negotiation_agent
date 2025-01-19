# Commodity Market Negotiation System

This project is a practice exercise to understand negotiation for multi-agent systems using the NB3 algorithm.

The source code and libraries have been obtained from [NB3: Negotiation Based Branch and Bound](https://www.iiia.csic.es/~davedejonge/nb3/).

## What is NB3?

NB3 is a generic algorithm for multilateral automated negotiations in environments where the number of possible deals is extremely large and the amount of available time is limited.

## Dependencies

To build and run this project, you need to have the following dependencies installed:

- Java (latest version)
- Maven (latest version)

## Installation and Build

To build the project, follow these steps:

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Build the project using Maven:

   ```sh
   mvn clean install
   ```

## Execution

To run the Commodity Market and the five agents, execute the following command:

```sh
java -cp target/commodity-market-1.0-SNAPSHOT.jar commodityMarket.agent.RunMarketAndFiveAgents
```

## Libraries

The project depends on the following libraries:

- commons-net-3.3.jar
- NB3-1.5.jar
- NegotiationServer-1.0.jar

These libraries are included in the `lib` directory and are referenced in the `pom.xml` file. Ensure that these dependencies are correctly placed in the `lib` directory before building the project.

## Credits

This project uses the NB3 algorithm developed by Dave de Jonge and Carles Sierra. For more information, visit [NB3: Negotiation Based Branch and Bound](https://www.iiia.csic.es/~davedejonge/nb3/).

- Dave de Jonge: [Website](http://www.iiia.csic.es/~davedejonge), [Email](mailto:davedejonge@iiia.csic.es)
- Carles Sierra: [Website](http://www.iiia.csic.es/~sierra), [Email](mailto:sierra@iiia.csic.es)

This project is for educational purposes to understand negotiation for multi-agent systems.
