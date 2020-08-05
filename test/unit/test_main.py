from fastapi.testclient import TestClient
import sys

sys.path.insert(1,'/home/yash/YoutubeNLP/Backend/') #Please Change this :P

from main import app

client = TestClient(app)

out = {"api_specification":{"prod":{"description":"Returns generated Specification","endpoint":["http://localhost/docs","http://localhost/redoc"]},"dev":{"description":"Returns standard API refrence","endpoint":"https://app.swaggerhub.com/apis-docs/youtubenlp/backend/0.0.1"}},"transcript_service":{"description":"Returns list of transcripts from video","endpoint":"http://localhost/transcripts/{video_id}"},"comment_service":{"description":"Returns list of comments from video","endpoint":"http://localhost/comments/{video_id}?q={k_top_comments}{&type, order}"},"video_service":{"description":{"description":"Returns the description text of the video","endpoint":"http://localhost/video/{video_id}{/description}"},"details":{"description":"Returns various detials related to video","endpoint":"http://localhost/video/{video_id}"},"keywords":{"description":"Returns a list of keywords related to video","endpoint":"http://localhost/video/{video_id}{/keywords}"}}}
def test_root():
   	response = client.get("/")
   	assert response.status_code == 200
def test_keywords():
	response = client.get("/video/2DG3pMcNNlw/keywords")
	assert response.status_code == 200
	assert response.json() == {"keywords":["CNBC","tom chitty","5g mobile","mobile world congress","sk telecom","telecom industry","5g network","5g wifi","5g technologvy","5g technology danger","telecommunications engineering","when will we get 5g","5g cell phone","4g cell phone","4g 5g differences","5g cell towers","5g cellular","5g connections","cnbc explains","5g chem trails","5g mobile phones in india","5g mobile phones","5g technology what you need to know"]}
def test_description():
        response = client.get("/video/2DG3pMcNNlw/description")
        assert response.status_code == 200
        assert response.json() == {"description":"5G is a new, faster network with the potential to completely transform the internet. So what makes it so revolutionary? CNBC’s Tom Chitty explains.\n\n-----\n\nSubscribe to us on YouTube: http://cnb.cx/2wuoARM\n\nSubscribe to CNBC Life on YouTube: http://cnb.cx/2wAkfMv\n\nLike our Facebook page:\nhttps://www.facebook.com/cnbcinternational\n\nFollow us on Instagram:\nhttps://www.instagram.com/cnbcinternational/\n\nFollow us on Twitter:\nhttps://twitter.com/CNBCi"}
def test_transcript():
        response = client.get("/transcripts/2DG3pMcNNlw")
        assert response.status_code == 200
        assert response.text == '["That is 4G - the mobile network\\nthat\'s used around the world","to make calls, send messages\\nand surf the web.","Now there are plans for 4G to\\nbe replaced by, you guessed it,","5G - a new, faster network that has\\nthe potential to transform the internet.","5G is a software defined network - it means\\nthat while it won’t replace cables entirely","it could replace the need for them by\\nlargely operating on the cloud instead.","This means it will have a\\n100x better capacity than 4G -","which will dramatically\\nimprove internet speeds.","For example, to download a two-hour film\\non 3G would take about 26 hours,","on 4G you’d be waiting 6 minutes,","and on 5G you’ll be ready to watch your\\nfilm in just over three and a half seconds.","But it’s not just internet capacity\\nthat will be upgraded.","Response times will\\nalso be much faster.","The 4G network responds to our commands\\nin just under 50 milliseconds.","With 5G it will take around one millisecond -\\n400 times faster than a blink of the eye.","Smartphone users will enjoy a\\nmore streamlined experience","but for a world that is increasingly dependant\\non the internet just to function,","a reduction in time delay is critical.","Self-driving cars, for example,\\nrequire a continuous stream of data.","The quicker that information is delivered to autonomous\\nvehicles, the better and safer, they can run.","For many analysts this is\\njust one example of how 5G","could become the connective\\ntissue for the internet of things,","an industry that’s set to grow threefold by 2025,\\nlinking and controlling not just robots,","but also medical devices, industrial\\nequipment and agriculture machinery.","5G will also provide a much more personalized web\\nexperience using a technique called network slicing.","It’s a way of creating separate\\nwireless networks on the cloud,","allowing users to create\\ntheir own bespoke network.","For instance, an online gamer needs faster\\nresponse times and greater data capacity","than a user that just wants\\nto check their social media.","Being able to personalize the internet\\nwill also benefit businesses.","At big events like Mobile World Congress for\\nexample - there is a mass influx of people","in one particular area using\\ndata-heavy applications.","But with 5G, organizers could pay for\\nan increased slice of the network,","boosting its internet capacity and thus\\nimproving its visitors’ online experience.","So when can we start using 5G?","Well, not yet and according to\\nsome analysts not until 2020.","5G was created years ago and\\nhas been talked up ever since.","Yet it’s estimated that even by 2025,\\nthe network will still lag behind","both 4G and 3G in terms of\\nglobal mobile connections.","Its mainstream existence\\nfaces multiple hurdles.","The most significant of\\nthese of course is cost.","According to some experts, 5G\\ncould cause network operators","to tear up their current business\\nmodels for it to make business sense.","In the U.K. for example, 3G and 4G networks\\nwere relatively cheap to set up","because they were able to roll out on existing\\nfrequencies, on the country’s radio spectrum.","For 5G to work properly however, it needs\\na frequency with much bigger bandwidth","which would require\\nbrand new infrastructure.","Some analysts believe that the extensive\\nbuilding and running costs will force","operators to share the use and\\nmanagement of the mobile network.","This has been less of an obstacle for countries like\\nChina, who are taking a more coherent approach.","The government, operators and\\nlocal companies such as Huawei","and ZTE","are about to launch big 5G trials\\nthat would put them at the forefront","of equipment production\\nfor the new technology.","That may be at the expense of the West, where\\nthere is concern regarding Asia’s 5G progress.","A leaked memo from the National\\nSecurity Council to the White House","called for a nationalized 5G network to keep\\nthe U.S. ahead of their global competitors.","White House officials dismissed the idea,\\nbut some experts predict that by 2025","nearly half of all mobile connections\\nin the U.S. will be 5G,","a greater percentage than\\nany other country or region.","It’s still likely however that much of the West\\nwill have a more gradual approach to 5G,","driven by competition but with\\na patchy style of development.","For example, AT&T pledged to start rolling out\\n5G later this year but in just a handful of cities.","For key industrial zones however, it’s predicted\\nthe technology will be adopted quickly,","while for many in rural areas\\n5G may be a long way off.","But when 5G does establish itself\\nand fulfills its supposed potential,","it could even change how we get\\nthe internet at home and at work -","with the wireless network replacing the\\ncurrent system of phone lines and cables.","It may not happen overnight,\\nbut 5G is coming.","Hi guys, thank you for watching.","If you\'d like to see more of our\\ntech videos then check out these.","Otherwise comment below the video for any\\nfuture explainers you\'d like us to make,","and remember don\'t forget to subscribe.","Thanks for watching!"]'

def test_root():
        response = client.get("/")
        assert response.status_code == 200
def test_worldcloud():
        response = client.get("/world-cloud​/2DG3pMcNNlw")
        assert response.status_code == 200
def test_sentiments_details():
        response = client.get("/sentiments/2DG3pMcNNlw")
        assert response.status_code == 200
def test_controversial():
        response = client.get("/comments/2DG3pMcNNlw/controversial")
        assert response.status_code == 200
def test_emotions():
        response = client.get("/emotions/2DG3pMcNNlw/score")
        assert response.status_code == 200
def test_lda():
        response = client.get("/lda​/2DG3pMcNNlw")
        assert response.status_code == 200
def test_ner_targeted():
        response = client.get("/ner/2DG3pMcNNlw/targeted")
        assert response.status_code == 200

def test_ner_sentiments():
        response = client.get("/sentiments/2DG3pMcNNlw/score")
        assert response.status_code == 200
