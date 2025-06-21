import { StackContext, Api, Function, Table } from "sst/constructs";

export function SecEdgarStack({ stack }: StackContext) {
  // DynamoDB table (optional, for storing filings)
  const filingsTable = new Table(stack, "Filings", {
    fields: {
      id: "string",
      cik: "string",
      filingDate: "string",
      data: "string",
    },
    primaryIndex: { partitionKey: "id" },
  });

  // Lambda function (Python 3.11 runtime)
  const secEdgarLambda = new Function(stack, "SecEdgarExtractor", {
    handler: "src/lambda/handler.main", // path to your Python handler
    runtime: "python3.11",
    environment: {
      TABLE_NAME: filingsTable.tableName,
    },
    permissions: [filingsTable], // grant Lambda access to the table
    timeout: 30,
  });

  // API Gateway
  const api = new Api(stack, "Api", {
    defaults: {
      function: {
        bind: [filingsTable],
      },
    },
    routes: {
      "POST /extract": secEdgarLambda,
    },
    cors: {
      allowMethods: ["POST"],
      allowOrigins: ["*"], // restrict in production!
    },
  });

  stack.addOutputs({
    ApiEndpoint: api.url,
    TableName: filingsTable.tableName,
  });
}

