using Microsoft.VisualStudio.TestTools.UnitTesting;
using Moq;
using System;

namespace ProgramTests
{
    [TestClass]
    public class ProgramTests
    {
        private const string aiSvcKey = "invalid_key";
        private const string aiSvcEndpoint = "https://fakeendpoint.cognitiveservices.azure.com";

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void GetLanguage_InvalidTextThrowsArgumentException()
        {
            // Arrange
            string text = null;

            // Act
            Program.GetLanguage(text);
        }

        [TestMethod]
        [ExpectedException(typeof(RequestFailedException))]
        public void GetLanguage_InvalidCredentialsThrowsRequestFailedException()
        {
            // Arrange
            string text = "Hello, world!";

            // Mock the TextAnalyticsClient to throw a RequestFailedException
            var mockClient = new Mock<TextAnalyticsClient>(MockBehavior.Strict);
            mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>())).Throws(new RequestFailedException("Invalid credentials", 401));

            // Replace the default client creation with the mocked one
            var originalCreateClient = Program.CreateClient;
            Program.CreateClient = () => mockClient.Object;

            try
            {
                // Act
                Program.GetLanguage(text);
            }
            finally
            {
                // Restore the original client creation method
                Program.CreateClient = originalCreateClient;
            }
        }

        [TestMethod]
        [ExpectedException(typeof(RequestFailedException))]
        public void GetLanguage_ServiceDownThrowsRequestFailedException()
        {
            // Arrange
            string text = "Hello, world!";

            // Mock the TextAnalyticsClient to throw a RequestFailedException due to service unavailability
            var mockClient = new Mock<TextAnalyticsClient>(MockBehavior.Strict);
            mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>())).Throws(new RequestFailedException("Service unavailable", 503));

            // Replace the default client creation with the mocked one
            var originalCreateClient = Program.CreateClient;
            Program.CreateClient = () => mockClient.Object;

            try
            {
                // Act
                Program.GetLanguage(text);
            }
            finally
            {
                // Restore the original client creation method
                Program.CreateClient = originalCreateClient;
            }
        }
    }

    public static class ProgramExtensions
    {
        public static TextAnalyticsClient CreateClient(this Program program)
        {
            AzureKeyCredential credentials = new AzureKeyCredential(aiSvcKey);
            Uri endpoint = new Uri(aiSvcEndpoint);
            return new TextAnalyticsClient(endpoint, credentials);
        }
    }
}