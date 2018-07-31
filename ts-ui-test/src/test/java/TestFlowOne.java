import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;


public class TestFlowOne {
    @BeforeClass
    public void setUp() throws Exception {
        //do nothing
    }

    @Test
    public void testLogin()throws Exception {

        RestTemplate restTemplate = new RestTemplate();

        HttpEntity requestEntity = new HttpEntity(null, new HttpHeaders());
        ResponseEntity<Boolean> re = restTemplate.exchange(
                "http://10.141.212.23:30085/cancelOrder/setRecheck/true",
//                "http://10.141.212.22:18885/cancelOrder/setRecheck/true",
                HttpMethod.GET,
                requestEntity,
                Boolean.class);

        System.out.println("：" + re.getBody().booleanValue());
        Assert.assertEquals(re.getBody().booleanValue(), true);

        for (int i = 0; i < 10; i++) {
            Thread.sleep(7000);
            HttpEntity requestEntity2 = new HttpEntity(null, new HttpHeaders());
            ResponseEntity<CancelOrderResult> cancel = restTemplate.exchange(
                    "http://10.141.212.23:30085/cancelOrder/5ad7750b-a68b-49c0-a8c0-32776b067703",
                    HttpMethod.GET,
                    requestEntity2,
                    CancelOrderResult.class);
            System.out.println(cancel.getBody().getMessage());
            Assert.assertEquals(cancel.getBody().isStatus(), true);
        }

    }


    @AfterClass
    public void tearDown() throws Exception {
        RestTemplate restTemplate = new RestTemplate();
        HttpEntity requestEntity = new HttpEntity(null, new HttpHeaders());
        for (int i = 0; i < 20; i++) {
            Thread.sleep(5000);
            ResponseEntity<Boolean> cancel = restTemplate.exchange(
                    "http://10.141.212.23:30085/cancelOrder/setRecheck/false",
                    HttpMethod.GET,
                    requestEntity,
                    Boolean.class);
        }
    }
}
