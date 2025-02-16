using Microsoft.VisualStudio.TestTools.UnitTesting;
using Moq;
using System;

namespace UnitTests
{
    [TestClass]
    public class ProgramTests
    {
        private const string AISvcKey = "your_key_here";
        private const string AISvcEndpoint = "your_endpoint_here";

        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void GetLanguage_NullText_ThrowsArgumentNullException()
        {
            Program.GetLanguage(null);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void GetLanguage_EmptyText_ThrowsArgumentException()
        {
            Program.GetLanguage("");
        }

        [TestMethod]
        [ExpectedException(typeof(RequestFailedException))]
        public void GetLanguage_FailureResponse_ThrowsRequestFailedException()
        {
            var mockClient = new Mock<TextAnalyticsClient>();
            mockClient.Setup(client => client.DetectLanguage(It.IsAny<string>())).Throws(new RequestFailedException("Test failure"));

            var program = new Program();
            program.AISvcKey = AISvcKey;
            program.AISvcEndpoint = AISvcEndpoint;
            program.client = mockClient.Object;

            program.GetLanguage("test text");
        }
    }
}